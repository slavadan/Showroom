FROM python:3.9

RUN mkdir -p /docker
WORKDIR /docker

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /docker
RUN pip install -r requirements.txt