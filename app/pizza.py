'''
File: pizza.py
Author: April Sigda
Purpose: Handles all interactions invoked from the pizza management
    interface
'''
from flask import Blueprint, request, flash, redirect, url_for
from .models import Pizza, PizzaToppings
from .database import db

pizza = Blueprint('pizza', __name__)

# Return a list of all pizzas.
def get_pizzas():
    return Pizza.query.all()

# Return a list of all toppings that are on the given pizza.
# Parameters:
# - p (Pizza): the Pizza object to get the toppings for
# Returns:
# - A list containing the internal ID of each topping
#   associated with the pizza
def get_pizza_toppings(p: Pizza):
    query = db.select(PizzaToppings.topping).where(PizzaToppings.pizza == p.id)
    return db.session.execute(query).scalars().all()

# Remove all pizza-topping records for the given pizza.
# Parameters:
# - p (Pizza): the Pizza object to remove the toppings for
def delete_pizza_toppings(p: Pizza):
    map(db.session.delete, PizzaToppings.query.filter_by(pizza=p.id))

# Return the lists of toppings for all pizzas in the database.
# Returns:
# - A 2D list containing the lists of toppings for each pizza,
#   ordered by pizza ID number
def get_all_pizza_toppings():
    return list(map(get_pizza_toppings, get_pizzas()))

# Since HTML forms only support GET and POST, we use a hidden
# field to distinguish POST, PUT, and DELETE
@pizza.route('/pizza', methods=['POST'])
def post_pizza():
    method = request.form.get('_method')
    if method == 'POST':
        return add_pizza(request)
    elif method == 'PUT':
        return edit_pizza(request)
    elif method == 'DELETE':
        return delete_pizza(request)
    return "error"

# Adds the toppings from the request body to the given pizza
# Parameters:
# - 'pizza' (Pizza): the Pizza object to add the toppings to
# Request body parameters:
# - 'toppings' (string list): the list of topping IDs to add
def add_pizza_toppings(pizza, request):
    pid = Pizza.query.filter_by(name=pizza).first().id
    for topping in request.form.getlist('topping'):
        new_link = PizzaToppings(pizza=pid, topping=topping)
        db.session.add(new_link)
    db.session.commit()

# Add a new pizza to the database. Does not allow duplicate
# pizza names
# Request body parameters:
# - 'newname' (string): the name of the new pizza
# - 'topping' (string list): the IDs of all toppings to be added to
#   the new pizza
# Returns:
# - Redirect to the home page. Displays a success or error message
def add_pizza(request):
    name = request.form.get('newname')
    if Pizza.query.filter_by(name=name).first() is not None:
        flash('Error: cannot add duplicate pizza ' + name, 'danger')
    else:
        new_pizza = Pizza(name=name)
        db.session.add(new_pizza)
        db.session.commit()
        add_pizza_toppings(name, request)
        flash('Success: added pizza ' + name, 'success')
    return redirect(url_for('pages.home'))

# Edit a pizza in the database. Does not allow duplicate pizza
# names. Supports editing both name and toppings.
# Request body parameters:
# - 'item' (string): the internal ID number of the pizza to edit
# - 'newname' (string): the updated name for the selected pizza
# - 'topping' (string list): the IDs of all toppings on the pizza
# Returns:
# - Redirect to the home page. Displays a success or error message
def edit_pizza(request):
    id = request.form.get('item')
    newname = request.form.get('newname')
    pizza = Pizza.query.get(id)
    if pizza is None:
        flash('Error: pizza not found', 'danger')
    elif newname != pizza.name and Pizza.query.filter_by(name=newname).first() is not None:
        flash('Error: cannot add duplicate pizza ' + newname, 'danger')
    else:
        pizza.name = newname
        old_toppings = get_pizza_toppings(pizza)
        new_toppings = request.form.getlist('topping')
        for topping in old_toppings:
            if topping not in new_toppings:
                pizzatopping = PizzaToppings.query.filter_by(pizza=id, topping=topping).first()
                db.session.delete(pizzatopping)
        for topping in new_toppings:
            if topping not in old_toppings:
                pizzatopping = PizzaToppings(pizza=id, topping=topping)
                db.session.add(pizzatopping)
        db.session.commit()
        flash('Success: updated pizza ' + newname, 'success')
    return redirect(url_for('pages.home'))

# Removes a pizza from the database
# Request body parameters:
# - 'item' (string): the internal ID number of the pizza to delete
# Returns:
# - Redirect to the home page. Displays a success or error message
def delete_pizza(request):
    id = request.form.get('item')
    pizza = Pizza.query.get(id)
    if pizza is None:
        flash('Error: pizza not found', 'danger')
    else:
        db.session.delete(pizza)
        delete_pizza_toppings(pizza)
        db.session.commit()
        flash('Success: removed pizza ' + pizza.name, 'success')
    return redirect(url_for('pages.home'))