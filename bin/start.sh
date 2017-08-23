!#/bin/bash

docker build -t restaurant-service-flask . && \
docker run -p 8080:8080 restaurant-service-flask gunicorn start:app -w 3 -b :8080
