'''
File: models.py
Author: April Sigda
Purpose: Defines the model classes that are used in the application.
    SQLAlchemy uses these to generate the requisite database tables.
    They are also used to translate the corresponding Python objects
    to database rows.
'''
from flask_login import UserMixin
from .database import db

# User model
# Fields:
# - id (int): internal identifier for the object.
#       this is the primary key for the db table
# - username (string): the user's username. must be unique
# - password (string): the hashed and salted password string
#       for the user
# - role (string): the user's job role. This should be either
#       'chef' or 'manager'
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(100))

# Topping model
# Fields:
# - id (int): internal identifier for the object.
#       this is the primary key for the db table
# - name (string): the name of the topping. must be unique
class Topping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

# Pizza model
# Fields:
# - id (int): internal identifier for the object.
#       this is the primary key for the db table
# - name (string): the name of the pizza. must be unique
class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

# Pizza Topping model. Stores a mapping between one pizza
#   and one topping, to indicate that the topping is on the pizza
# Fields:
# - id (int): internal identifier for the object.
# - topping (int): ID key of the topping object
# - pizza (int): ID key of the pizza object
class PizzaToppings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topping = db.Column(db.Integer, db.ForeignKey('topping.id'))
    pizza = db.Column(db.Integer, db.ForeignKey('pizza.id'))