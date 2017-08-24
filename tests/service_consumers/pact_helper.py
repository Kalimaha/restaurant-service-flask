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
