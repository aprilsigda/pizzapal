from ..models import Topping, PizzaToppings
from . import db

def get_toppings():
    return db.session.select(Topping)

def add_topping():
    return

def edit_topping():
    return

def delete_topping():
    return