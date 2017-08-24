!#/bin/bash
docker build --no-cache -t restaurant-service-flask . && docker run restaurant-service-flask pact-test verify consumers
