FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN apt-get update

RUN pip install -r requirements.txt

CMD ["python", "-m", "./main.py"]
