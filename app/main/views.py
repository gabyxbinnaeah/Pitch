
from flask import render_template,request,redirect,url_for,abort, flash
from . import main
from flask_login import login_required, current_user
from ..models import Pitch, User,PitchComments,Upvotes,Downvotes
from .forms import PitchForm,PitchCommentsForm,UpvotesForm,DownvotesForm
from flask.views import View,MethodView
from .. import db
import markdown2 

#Views
@main.route('/', methods= ['GET','POST'])
def index():
    '''
    view page function that returns index page and its data
    '''
    pitch=Pitch.query.filter_by().first() 
    title='Home'
    businesspitch=Pitch.query.filter_by(category="businesspitch")
    interviewpitch=Pitch.query.filter_by(category="interviewpitch")
    politicalpitch=Pitch.query.filter_by(category="politicalpitch")
    religiouspitch=Pitch.query.filter_by(category="religiouspitch") 

    upvotes=Upvotes.get_all_upvotes(pitch_id=Pitch.id)  

    return render_template('home.html',title=title,pitch=pitch,businesspitch=businesspitch,interviewpitch=interviewpitch,politicalpitch=politicalpitch,religiouspitch=religiouspitch)

    
