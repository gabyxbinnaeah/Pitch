from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import UserMixin
# from . import login_manager 
from datetime import datetime 


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id)) 

class Pitch(db.Model):
    '''
    properties of pitch class
    '''
    __tablename__='pitches' 

    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String())
    category=db.Column(db.String(255), nullable=False)
    description=db.Column(db.String(255), index=True)
    pitchescomment=db.relationship('PitchComments',backref ='pitchescomment',lazy= "dynamic")
    date_posted=db.Column(db.DateTime,default=datetime.utcnow)
    upvotes=db.relationship('Upvotes', backref ='user',lazy= "dynamic")
    downvotes=db.relationship('Downvotes',backref='user',lazy= "dynamic")

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
    pitch_id=db.Column(db.Integer,db.ForeignKey("pitches.id"))
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    description=db.Column(db.String())  
    date_posted=db.Column(db.DateTime,default=datetime.utcnow) 


class  Upvotes(db.model):
    id=db.Column(db.Integer,)
    upvote=db.Column(db.Integer,default=1)
    pitch_id=db.Column(db.Integer,db.ForeignKey("pitches.id")) 
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))  

    def save_upvotes(self):
        db.session.add(self)
        db.session.commit() 

    def add_upvotes(cls,id):
        upvote_pitch= Upvotes(user=current_user,pitch_id=id) 
        upvote_pitch.save_upvotes()

    @classmethod
    def get_upvotes(cls,id):
        upvote=Upvote.query.filter_by(pitch_id=id).all()

    @classmethod
    def get_all_upvotes(cls,id):
        upvotes=Upvotes.query.order_by('id').all()
        return Upvotes

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'

class Downvotes(db.model):
    id=db.Column(db.Integer,primary_key=True)
    downvotes=db.Column(db.Integer,default=1)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id")) 
    pitch_id=db.Column(db.Integer,db.ForeignKey("pitches.id"))

    def save_downvote(self):
        db.session.add(self)
        db.session.commit()

    
  



class User(UserMixin, db.Model):
    '''
    models that dfeines properties of user class
    '''
    __tablename__="users"

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(),unique = True,index = True)
    password_hash=db.Column(db.String(255))
    pitches=db.relationship('Pitch', backref ='user',lazy= "dynamic")
    pitchcomments=db.relationship('PitchComments',backref ='user',lazy= "dynamic")
    downvotes=db.relationship('Downvotes',backref='user',lazy= "dynamic")
    upvotes=db.relationship('Upvotes',backref='user',lazy= "dynamic")


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


class Role(db.Model):
    '''
    defines the role of each user in the user model 
    '''

    __tablename__="roles"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30))
    users = db.relationship('User',backref='users',lazy= "dynamic")
        #method returns a string containing a printable representation of an object.
    def __repr__(self):
        return f'User {self.name}' 

class PhotoProfile(db.Model):
    '''
    model that defines profile photos for user account
    '''
    __tablename__ ="photos"

    id=db.Column(db.Integer,primary_key=True)
    pic_path=db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
      





    
    

