from pact_test import *


@honours_pact_with('PythonEats')
@pact_uri('http://localhost:9292/pacts/provider/PyzzaHut/consumer/PythonEats/latest')
class PythonEats(ServiceConsumerTest):

    @state('some pizzas exist')
    def test_pizzas_exist(self):
        pass

    @state('a pizza exists')
    def test_pizza_exist(self):
        pass
