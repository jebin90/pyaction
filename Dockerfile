FROM python:3.8

WORKDIR /app
COPY . /app

RUN apt-get update && \
    apt-get install -y python3-fenics

RUN pip install -r requirements.txt

CMD ["python", "-m", "unittest", "discover", "-v"]
