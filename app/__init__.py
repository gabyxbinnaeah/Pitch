from flask import Flask
from flask_bootstrap import Bootstrap 
from config import config_options

bootstrap=Bootstrap()
#initializing app
app=Flask(__name__)

bootstrap.init_app(app) 
