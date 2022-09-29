import dependencies
from flask import Blueprint
from  __index__ import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'Login'

@auth.route('/signup')
def signup():
    return 'Signup'

@auth.route('/logout')
def logout():
    return 'Logout'

@auth.route('/create')
def create():
    return 'create'

@auth.route('/edit')
def edit():
    return 'edit'