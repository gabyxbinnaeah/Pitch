from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import UserMixin
from . import login_manager 
from datetime import datetime 


@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(int(user_id))

class Quote:
    '''
    quote class that define quote objects
    '''
    def __init__(self,id,author,quote):
        self.id = id
        self.author = author
        self.quote = quote
        

class Pitch(db.Model):
    '''
    properties of pitch class
    '''
    __tablename__='pitches' 

    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    title=db.Column(db.String())
    category=db.Column(db.String(255), nullable=False)
    description=db.Column(db.String(255), index=True)
    email = db.Column(db.String(255),unique = True,index = True)
    pitchescomment=db.relationship('PitchComments',backref ='pitchescomment',lazy= "dynamic")
    date_posted=db.Column(db.DateTime,default=datetime.utcnow)
    upvotes=db.relationship('Upvotes', backref ='downvote',lazy= "dynamic")
    downvotes=db.relationship('Downvotes',backref='upvote',lazy= "dynamic")  

    @classmethod
    def get_pitches(cls,id):
        pitches=Pitch.query.order_by(pitch_id=id).desc().all()
        return pitches

    def  __repr__(self):
        return f'Pitch {self.description}'

class PitchComments(db.Model):
    '''
    model that defines the properties of comments
    '''
    __tablename__='comments'

    id=db.Column(db.Integer,primary_key=True)
    description=db.Column(db.String())  
    date_posted=db.Column(db.DateTime,default=datetime.utcnow) 
    pitch_id=db.Column(db.Integer,db.ForeignKey("pitches.id"))
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))


class  Upvotes(db.Model):

    __tablename__="upvotes"

    id=db.Column(db.Integer,primary_key=True)
    upvote=db.Column(db.Integer,default=1)
    pitch_id=db.Column(db.Integer,db.ForeignKey("pitches.id")) 
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))  

    def save_upvotes(self):
        db.session.add(self)
        db.session.commit()

    def add_upvote(cls,id):
        upvote_pitch=Upvotes(user_id=current_user, pitch_id=id)
        upvote_pitch.save_upvotes() 
    
    @classmethod
    def get_upvotes(cls,id):
        upvote=Upvotes.query.filter_by(pitch_id=id).all()

    @classmethod
    def get_all_upvotes(cls,pitch_id):
        upvotes=Upvotes.query.order_by("id").all() 
        return upvotes

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'

class Downvotes(db.Model):
    __tablename__ ="downvotes"

    id=db.Column(db.Integer,primary_key=True)
    downvotes=db.Column(db.Integer,default=1)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id")) 
    pitch_id=db.Column(db.Integer,db.ForeignKey("pitches.id"))

    def save_downvotes(self):
        db.session.add(self)
        db.session.commit()

    def add_downvote(cls,id):
        downvotes=Downvotes(user=current_user, pitch_id=id)
        downvotes.save_downvotes() 
    
    @classmethod
    def get_downvotes(cls,id):
        downvotes=Downvotes.query.filter_by(pitch_id=id).all()

    @classmethod
    def get_all_downvotes(cls,pitch_id):
        downvotes=Downvotes.query.order_by("id").all() 
        return downvotes

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
    
  



class User(UserMixin, db.Model):
    '''
    models that dfeines properties of user class
    '''
    __tablename__="users"

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(),unique = True,index = True)
    profile_pic_path = db.Column(db.String())
    bio = db.Column(db.String(255))
    password_hash=db.Column(db.String(255))
    pitches=db.relationship('Pitch', backref ='pitches',lazy= "dynamic")
    pitchcomments=db.relationship('PitchComments',backref ='pitchcomment',lazy= "dynamic")
    downvotes=db.relationship('Downvotes',backref='dislikes',lazy= "dynamic")
    upvotes=db.relationship('Upvotes',backref='likes',lazy= "dynamic")


    @property
    def password(self):
        raise AttributeError('You can not acess  the password attribute')

    @password.setter
    def  password(self,password):
        self.password_hash=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    
    def __repr__(self):
        return f'User {self.username}'

 


      





    
    

