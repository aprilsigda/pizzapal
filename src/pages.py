from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from . import models

pages = Blueprint('pages', __name__)

@pages.route('/')
def index():
    return redirect(url_for('pages.home'))

@pages.route('/home')
def home():
    if not current_user.is_authenticated:
        return redirect('/login')
    elif current_user.role == 'chef':
        return render_template('chefhome.html')
    elif current_user.role == 'manager':
        return render_template('managerhome.html', toppings=models.Topping.query.all())