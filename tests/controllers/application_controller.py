from json import loads
from json import dumps
from service.controllers.application_controller import app


def test_get_menu():
    tester = app.test_client()
    response = tester.get('/')
    json = loads(response.data.decode('utf-8'))

    expected_json = [{'id': 42, 'name': 'Spam & Eggs', 'price': 15.0}]

    assert json == expected_json


def test_get_menu_item():
    tester = app.test_client()
    response = tester.get('/42/')
    json = loads(response.data.decode('utf-8'))

    expected_json = {'id': 42, 'name': 'Spam & Eggs', 'price': 15.0}

    assert json == expected_json
