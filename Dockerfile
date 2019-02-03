FROM python:2.7-slim

MAINTAINER Kathryn S Remivasan

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
