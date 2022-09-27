import dependencies
from flask import Flask, Blueprint
#from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
#db = SQLAlchemy()

app = Flask(__name__)

#app.config['SECRET_KEY'] = 'secret-key-goes-here'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    
#db.init_app(app)



# blueprint for non-auth parts of app
app.register_blueprint(main_blueprint)


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Index2'

@main.route('/profile')
def profile():
    return 'Profile'

@main.route('/aboutme')
def aboutme():
    return 'Aboutme'

# blueprint for auth parts of app
app.register_blueprint(auth_blueprint)
auth = Blueprint('auth', __name__)

@auth.route('/login')
@auth.route('/login')
def login():
    return 'Login'

@auth.route('/signup')
def signup():
    return 'Signup'

@auth.route('/logout')
def logout():
    return 'Logout'