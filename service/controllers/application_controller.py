from flask import Flask
from flask import jsonify
from flask import make_response


app = Flask(__name__)


@app.route('/pizzas/<pizza_type>/')
def get_pizza(pizza_type):
    if pizza_type == 'hawaiian':
        return jsonify({'message': 'we do not serve pineapple with pizza'}), 404
    return jsonify({'id': 42, 'type': pizza_type})


@app.route('/orders/', methods=['POST'])
def place_order():
    return make_response(jsonify({'id': 123}), 201)
