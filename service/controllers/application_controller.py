from flask import Flask
from flask import jsonify
from service.repositories.menu_repository import MenuRepository


app = Flask(__name__)


@app.route('/')
def menu_service():
    menu = MenuRepository.get()
    menu_dict = [menu_item.__dict__ for menu_item in menu]
    return jsonify(menu_dict)


@app.route('/<menu_item_id>/')
def menu_item_service(menu_item_id):
    menu = MenuRepository.get_item(menu_item_id)
    return jsonify(menu.__dict__)
