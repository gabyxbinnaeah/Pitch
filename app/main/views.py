
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


@main.route('/pitches/new/', methods=['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    my_upvotes=Upvotes.query.filter_by(pitch_id=Pitch.id)
    if form.validate_on_submit():
        description=form.description.data
        title=form.title.data 
        user_id= current_user 
        category=form.category.data 
        new_pitch = Pitch(user_id =current_user._get_current_object().id, title = title,description=description,category=category)
        db.session.add(new_pitch)
        db.session.commit()
        

        return redirect(url_for('main.index')) 
    all_comments = PitchComments.query.filter_by(pitch_id = pitch_id).all()
    return render_template('pitches.html',form=form) 


@main.route('/pitch/upvote/<int:pitch_id>/upvote', methods=['GET','POST']) 
@login_required 
def upvote(pitch_id):
    pitch=Pitch.query.get(pitch_id)
    user=current_user
    pitch_upvotes=Upvotes.query.filter_by(pitch_id=pitch_id)

    if Upvotes.query.filter(Upvotes.user_id==user.id,Upvotes.pitch_id==pitch_upvotes).first():
        return redirect(url_for('main.index'))

    new_upvote=Upvotes(pitch_id=pitch_id, user =current_user)
    new_upvote= save_upvotes()
    return redirect(url_for('main.index')) 


@main.route('/pitch/downvote/<int:pitch_id>/downvote', methods = ['GET', 'POST'])
@login_required
def downvote(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    user = current_user
    pitch_downvotes = Downvotes.query.filter_by(pitch_id= pitch_id) 
    
    if Downvotes.query.filter(Downvotes.user_id==user.id,Downvotes.pitch_id==pitch_id).first():
        return  redirect(url_for('main.index'))


    new_downvote = Downvotes(pitch_id=pitch_id, user = current_user)
    new_downvote.save_downvotes()
    return redirect(url_for('main.index')) 

