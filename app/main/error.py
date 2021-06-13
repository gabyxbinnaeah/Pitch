from flask import render_template 
from . import main

@main.app_errorhandler(404)
def four_Ow_four():
    '''
    method that returns error if the url is not typed correctly.
    '''

    return render_template('fourOwfour.html'),404