FROM ubuntu:22.04
FROM python:3.7.7-slim

# 파이썬 환경을 위한 Selenium

WORKDIR /workdir/

RUN apt-get update && apt-get upgrade -y && apt-get install gcc g++ locales -y && locale-gen ko_KR.UTF-8
ENV LANG ko_KR.UTF-8
ENV LANGUAGE ko_KR:en
ENV LC_ALL ko_KR.UTF-8

COPY ./requirements.txt ./workdir/requirements.txt
COPY . /workdir/

RUN pip install --no-cache-dir -r requirements.txt
