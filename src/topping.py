from flask import Blueprint, request, flash, redirect, url_for
from .models import Topping, PizzaToppings
from .database import db

topping = Blueprint('topping', __name__)

@topping.route('/topping')
def get_toppings():
    return Topping.query.all()

@topping.route('/topping', methods=['POST'])
def post_topping():
    method = request.form.get('_method')
    if method == 'POST':
        return add_topping(request)
    elif method == 'PUT':
        return edit_topping(request)
    elif method == 'DELETE':
        return delete_topping(request)
    return "error"


def add_topping(request):
    name = request.form.get('newname')
    if Topping.query.filter_by(name=name).first() is not None:
        flash('Error: cannot add duplicate topping ' + name, 'danger')
    else:
        new_topping = Topping(name=name)
        db.session.add(new_topping)
        db.session.commit()
        flash('Success: added topping ' + name, 'success')
    return redirect(url_for('pages.home'))

def edit_topping(request):
    id = request.form.get('item')
    newname = request.form.get('newname')
    topping = Topping.query.filter_by(id=id).first()
    if topping is None:
        flash('Error: topping not found', 'danger')
    elif Topping.query.filter_by(name=newname).first() is not None:
        flash('Error: cannot add duplicate topping ' + newname, 'danger')
    else:
        topping.name = newname
        db.session.commit()
        flash('Success: updated topping to ' + newname, 'success')
    return redirect(url_for('pages.home'))

def delete_topping(request):
    id = request.form.get('item')
    topping = Topping.query.filter_by(id=id).first()
    if topping is None:
        flash('Error: topping not found', 'danger')
    else:
        db.session.delete(topping)
        db.session.commit()
        flash('Success: removed topping ' + topping.name, 'success')
    return redirect(url_for('pages.home'))