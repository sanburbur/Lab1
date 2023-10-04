
# !/usr/bin/env python3

import subprocess
import getpass

package_name = input("Введите имя пакета: ")

result = subprocess.run(['dpkg', '-s', package_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if result.returncode == 0:
    print("Информация о пакете:")
    print(result.stdout.decode())
else:
    print("Пакет не установлен")
    print("Поиск пакета в репозиториях...")

    result = subprocess.run(['apt-cache', 'search', package_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode == 0:
        print(result.stdout.decode())

        answer = input("Хотите установить пакет? (y/n): ")

        if answer == "y":
            password = getpass.getpass(prompt='Введите пароль от аккаунта sudo: ')
            subprocess.run(['sudo', '-S', 'apt-get', 'install', package_name], input=password.encode())
        else:
            print("Выход")
    else:
        print("Пакет не найден в репозиториях")
