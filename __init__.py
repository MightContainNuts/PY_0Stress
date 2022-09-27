import dependencies
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


app = Flask( __name__ )

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)

# blueprint for auth routes in our app
try: 
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    print ('success! - imported auth as blueprint')

except:
    print ('nope -auth-  that didna work')


# blueprint for non-auth parts of app

try: 
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    print ('success! - imported main as blueprint')

except:
    print ('nope - -main- that didna work')