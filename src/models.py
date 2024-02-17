from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

class Topping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Table())

class PizzaToppings(db.Model):
    topping = db.Column(db.Integer, db.ForeignKey('topping.id'))
    pizza = db.Column(db.Integer, db.ForeignKey('pizza.id'))