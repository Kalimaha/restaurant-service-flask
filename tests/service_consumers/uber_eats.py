from pact_test import *


@honours_pact_with('UberEats')
@pact_uri('http://guido-barbaglia.blog/src/pacts/bubba.json')
class UberEats(ServiceConsumerTest):

    @state('a pizza exists')
    def test_get_menu_item(self):
        pass
