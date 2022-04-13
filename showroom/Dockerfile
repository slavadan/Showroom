FROM python:3.9

RUN mkdir -p /showroom
WORKDIR /showroom

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /showroom
RUN pip install -r requirements.txt