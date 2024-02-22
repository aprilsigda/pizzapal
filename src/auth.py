'''
File: auth.py
Author: April Sigda
Purpose: Handles all authentication-related requests
'''
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from .database import db

auth = Blueprint('auth', __name__)

# Loads the login page
@auth.route('/login')
def login():
    return render_template('login.html')

# Logs in the current user. Uses the FlaskLogin library
# to keep track of the session
# Request parameters:
# - 'username' (string): the username of the user to log in
# - 'password' (string): the password of the user to log in
# NOTE: the way the password is handled is insecure! Currently
# it is transmitted to the server in plaintext before being hashed!
@auth.route('/login', methods=['POST'])
def login_post():
    uname = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=uname).first()
    if user is None or not check_password_hash(user.password, password):
        return redirect(url_for('auth.login'))

    login_user(user)
    return redirect(url_for('pages.home'))

# Loads the signup page. Note that in a real-world scenario,
# this page would likely not exist as creation of new users
# would require some kind of admin access
@auth.route('/signup')
def signup():
    return render_template('signup.html')

# Adds a new user to the database. Username must not already exist.
# Request parameters:
# - 'username' (string): the new user's username
# - 'password' (string): the new user's password
# NOTE: insecure! see login_post above
# - 'role' (string): the new user's role. Should be either 'chef' or 'manager'
# Returns:
# - Redirect to the login page after signup, or
#       to the signup page after failure
@auth.route('/signup', methods=['POST'])
def signup_post():
    uname = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')

    user = User.query.filter_by(username=uname).first()
    if user is not None:
        return redirect(url_for('auth.signup'))

    new_user = User(username=uname, password=generate_password_hash(password, method="pbkdf2"), role=role)

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

# Logs out the currently authenticated user and
# redirects to the login page
@auth.route('/logout')
def logout():
    logout_user()
    return redirect('/login')