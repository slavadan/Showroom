FROM python:3.9

RUN mkdir -p /home/slavadan/docker
WORKDIR /home/slavadan/docker

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /home/slavadan/docker
RUN pip install -r requirements.txt