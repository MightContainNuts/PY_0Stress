import dependencies
from flask import Blueprint
#from  import db

try:
    auth = Blueprint('auth', __name__)
    print ('auth bluprint')

except:
    print ('nah . auth bluprint')


@auth.route('/login')
def login():
    return 'Login'

@auth.route('/signup')
def signup():
    return 'Signup'

@auth.route('/logout')
def logout():
    return 'Logout'