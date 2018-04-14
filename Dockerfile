FROM ubuntu:latest

RUN apt update -y
RUN apt install -y python-pip
RUN pip install flask

COPY . /app
WORKDIR /app

EXPOSE 5000

ENTRYPOINT [ "python" ]
CMD ["flask-crawler/hello_world.py"]
