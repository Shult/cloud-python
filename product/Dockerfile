#FROM python:3-onbuild
#COPY . /usr/src/app
#CMD ["python", "api.py"]
#FROM python:3-onbuild
FROM ubuntu:latest

COPY . /usr/src/app
RUN apt-get update
RUN apt-get install -y python3.10
RUN apt-get install -y python3-pip
RUN pip install --ipv4 -r requirements.txt
CMD ["python", "api.py"]
