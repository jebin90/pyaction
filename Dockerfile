FROM python:3.8

WORKDIR /app
COPY main.py /app
COPY test_main.py /app

RUN apt-get update && \
    apt-get install -y fenics

RUN pip install -r requirements.txt

CMD ["python", "-m", "unittest", "discover", "-v"]
