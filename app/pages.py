'''
File: pages.py
Author: April Sigda
Purpose: Routes page requests to the proper locations
'''
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from . import models
from .pizza import *
from .topping import *

pages = Blueprint('pages', __name__)

# Redirects all requests for the root page to the homepage
@pages.route('/')
def index():
    return redirect(url_for('pages.home'))

# Routes requests to the '/home' endpoint.
# - if there is no user logged in: redirect to the login page
# - if the logged in user is a chef: display the pizza management page
# - if the logged in user is a manager: display the topping management page
@pages.route('/home')
def home():
    if not current_user.is_authenticated:
        return redirect('/login')
    elif current_user.role == 'chef':
        return render_template('chefhome.html', items=get_pizzas(), category='pizza', toppings=get_toppings(), pizzatoppings=get_all_pizza_toppings())
    elif current_user.role == 'manager':
        return render_template('managerhome.html', items=get_toppings(), category='topping')