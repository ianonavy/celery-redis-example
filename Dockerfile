FROM python:latest

RUN mkdir -p /opt/code
WORKDIR /opt/code

ADD ./requirements.txt /opt/code/requirements.txt
RUN pip install -r requirements.txt
