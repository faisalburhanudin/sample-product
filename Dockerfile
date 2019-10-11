FROM python:3.7.4-alpine3.10

WORKDIR /app

COPY ./requirements-prod.txt /app/requirements-prod.txt

RUN apk add --no-cache linux-headers alpine-sdk && \
    pip install uwsgi && \
    pip install -r requirements-prod.txt

COPY . /app

EXPOSE 9090

CMD uwsgi --http :9090 -w wsgi:wsgi