from ..models import Pizza, PizzaToppings
from . import db

def get_pizzas():
    return db.session.select(Pizza)

def get_pizza_toppings(p: Pizza):
    return db.session.select(PizzaToppings).where(PizzaToppings.c.pizza == p.id)

def add_pizza():
    return

def edit_pizza():
    return

def delete_pizza():
    return