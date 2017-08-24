!#/bin/bash
docker build --no-cache -t restaurant-service-flask . && docker run restaurant-service-flask pact-test verify consumers
#docker build -t restaurant-service-flask . && docker run -p 8080:8080 restaurant-service-flask pact-test verify consumers
