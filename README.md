[![Codefresh build status]( https://g.codefresh.io/api/badges/build?repoOwner=Kalimaha&repoName=restaurant-service-flask&branch=master&pipelineName=restaurant-service-flask&accountName=kalimaha&type=cf-1)]( https://g.codefresh.io/repositories/Kalimaha/restaurant-service-flask/builds?filter=trigger:build;branch:master;service:59e32084d2ab0a0001339b1f~restaurant-service-flask)
[![Codefresh build status]( https://g.codefresh.io/api/badges/build?repoOwner=Kalimaha&repoName=restaurant-service-flask&branch=master&pipelineName=restaurant-service-flask-2.7&accountName=kalimaha&type=cf-1)]( https://g.codefresh.io/repositories/Kalimaha/restaurant-service-flask/builds?filter=trigger:build;branch:master;service:59e41ad540f0d10001f4541f~restaurant-service-flask-2.7)

# Restaurant Service - Flask Version

Small web-app used to test the [pact-test](https://github.com/Kalimaha/pact-test) library.

## Available endpoints

* Menu: [http://localhost:8080/](http://localhost:8080/)
* Single Menu Item: [http://localhost:8080/42/](http://localhost:8080/42/)

## Setup for Pact Test

This web-app implements an hypothetical restaurant service which exposes two endpoints: one for the available menu and another one for single menu items. As a provider, this application needs to verify that it is honouring its pacts with the consumer(s).

### Pact Helper

This helper is used by Pact Test to start and stop the web-app before and after the tests. There are few rules associated to the helper:

* it **must** extends `PactHelper` class from `pact_test`
* it **must** implement the `setup` method
* it **must** implement the `tear_down` method

In addition to that, it is also possible to override default url (`localhost`) and port (`9999`) for the test. The following is a valid example of Pact Helper:

```python
import time
import subprocess
from pact_test import PactHelper


class RestaurantPactHelper(PactHelper):
    test_port = 8080

    process = None
    delay = 1

    def setup(self):
        self.process = subprocess.Popen('gunicorn start:app -w 3 -b :8080 --log-level error', shell=True)
        time.sleep(self.delay)

    def tear_down(self):
        self.process.kill()
```

This example starts and stops the web-app through [Gunicorn](http://gunicorn.org/) which is executed in a separate `subprocess`.

### State

When a consumer sets a pact, it defines certain states. States are basically pre-requisites to your test. Before honouring the pacts, a provider needs to define such states. For example:

```python
@honours_pact_with('UberEats')
@pact_uri('http://Kalimaha.github.io/src/pacts/pact.json')
class UberEats(ServiceConsumerTest):

    @state('some menu items exist')
    def test_get_menu_items(self):
        DB.save(MenuItem('spam'))
        DB.save(MenuItem('eggs'))
```

In this example, the provider stores some test data in its DB in order to make the system ready to receive mock calls from the consumer and therefore verify the pact.

### Run Pact Test

```
$ ./bin/pact.sh
```

This command will produce an output similar to the following:

```
[Pact Test for Python] - Test: UberEats
[Pact Test for Python] -   GIVEN some menu items exist UPON RECEIVING a request for a single menu item
[Pact Test for Python] -     status: PASSED
[Pact Test for Python] -   GIVEN some menu items exist UPON RECEIVING a request for an item which is not on the menu
[Pact Test for Python] -     status: FAILED
[Pact Test for Python] -       expected: {'error': 400}
[Pact Test for Python] -       actual:   {'error': 404}
[Pact Test for Python] -       message:  Body is incorrect
[Pact Test for Python] -
[Pact Test for Python] - Goodbye!
```

## Development

All the scripts below make use of [Docker](https://www.docker.com/). The base image is Alpine and Python 3.6.

### Test

```
$ ./bin/test.sh
```

### Run

```
$ ./bin/start.sh
```
