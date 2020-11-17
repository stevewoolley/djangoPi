FROM python:3.8-alpine
RUN apk add --update gcc libc-dev postgresql-dev
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
