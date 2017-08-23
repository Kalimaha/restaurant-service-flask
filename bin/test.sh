!#/bin/bash
docker build -t restaurant-service-flask . && docker run restaurant-service-flask python setup.py test
