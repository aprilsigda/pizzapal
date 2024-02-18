from flask_login import UserMixin
from .database import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(100))

class Topping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

class PizzaToppings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topping = db.Column(db.Integer, db.ForeignKey('topping.id'))
    pizza = db.Column(db.Integer, db.ForeignKey('pizza.id'))