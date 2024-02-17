from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/toppings')
def toppings():
    return

@api.route('/toppings', methods=['POST'])
def toppings_post():
    return

@api.route('/toppings', methods=['PUT'])
def toppings_put():
    return

@api.route('/toppings', methods=['DELETE'])
def toppings_delete():
    return

@api.route('/pizzas')
def pizzas():
    return

@api.route('/pizzas', methods=['POST'])
def pizzas_post():
    return

@api.route('/pizzas', methods=['PUT'])
def pizzas_put():
    return

@api.route('/pizzas', methods=['DELETE'])
def pizzas_delete():
    return

@api.route('/login', methods=['POST'])
def login_post():
    return