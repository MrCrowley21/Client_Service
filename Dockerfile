FROM python:3.7

WORKDIR /Client_Service

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5003

CMD ["python", "./server.py"]