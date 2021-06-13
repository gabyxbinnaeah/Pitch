from flask import Flask
from flask_bootstrap import Bootstrap 
from config import config_options
from flask_sqlalchemy import SQLAlchemy




bootstrap=Bootstrap()
db=SQLAlchemy()
#initializing app

def creat_app(configname):
    app=Flask(__name__)

    bootstrap.init_app(app) 

    #configuration options
    app.config.from_object(config_options[configname])
    
    from . import main as main_blueprint 
     #register blueprint
    app.register_blueprint(main_blueprint) 

    return app    


