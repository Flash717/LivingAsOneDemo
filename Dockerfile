FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python3 python3-dev python3-pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 8081

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]