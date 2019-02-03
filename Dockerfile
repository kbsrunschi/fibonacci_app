FROM ubuntu:16.04

MAINTAINER Kathryn Remivasan

RUN apt-get update -y && \
          apt-get install -y python-pip python-dev

RUN pip install --upgrade pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

EXPOSE 5000

CMD [ "app.py", "-n", "5000" ]
