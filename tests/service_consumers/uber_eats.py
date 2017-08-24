from pact_test import *


@has_pact_with('Restaurant Service')
@pact_uri('http://guido-barbaglia.blog/src/pacts/pact.json')
class UberEats(ServiceConsumerTest):

    @state('some menu items exist')
    def test_get_menu_item(self):
        # print()
        # print('\t\tHallo from the Restaurant Service!')
        # print('\t\tI am about to setup the system for the test...')
        # print('\t\t:: create menu ::')
        # print('\t\t:: create menu ::')
        # print('\t\t:: create menu ::')
        # print('\t\tDone! Rock and roll babe! 🤘')
        # print()
        pass
