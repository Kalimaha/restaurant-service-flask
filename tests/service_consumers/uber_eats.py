from pact_test import *


@has_pact_with('Restaurant Service')
@pact_uri('http://guido-barbaglia.blog/src/pacts/pact.json')
class UberEats(ServiceConsumerTest):

    @state('some menu items exist')
    def test_get_menu_item(self):
        pass
