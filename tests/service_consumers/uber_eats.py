from pact_test import *


@honours_pact_with('UberEats')
@pact_uri('http://guido-barbaglia.blog/src/pacts/pact.json')
class UberEats(ServiceConsumerTest):

    @state('some menu items exist')
    def test_get_menu_item(self):
        pass
