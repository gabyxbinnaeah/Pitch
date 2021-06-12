from flask import Flask
from flask_bootstrap import Bootstrap 

bootstrap=Bootstrap()
#initializing app
app=Flask(__name__)

bootstrap.init_app(app)