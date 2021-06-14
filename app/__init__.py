from flask import Flask
from flask_bootstrap import Bootstrap 
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_simplemde import SimpleMDE



# Instances of flask extensions
# Instance of LoginManger and using its methods
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
db = SQLAlchemy()
simple = SimpleMDE()
#initializing app

def create_app(configname):
    app=Flask(__name__)

    bootstrap.init_app(app)
    db.init_app(app) 

    #configuration options
    app.config.from_object(config_options[configname])
    
    from .main import main as main_blueprint 
     #register blueprint
    app.register_blueprint(main_blueprint) 

    return app    


