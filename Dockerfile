FROM python:3.11.6

WORKDIR /app

RUN pip install --upgrade pip

RUN apt-get update 

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8001

CMD ["python", "main.py"]