FROM ubuntu:latest

RUN apt-get update -y && apt-get install python3 -y && apt-get install python3-pip -y
WORKDIR /app
COPY requirements.txt .

RUN python3 -m pip install --no-cache-dir -r requirements.txt
COPY . .

ENTRYPOINT ["python3","main.py"]

