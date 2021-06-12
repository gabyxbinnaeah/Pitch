from . import db  
from werkzeug.security import generate_password_hash,check_password_hash 



class Pitch(db.Model):
    '''
    properties of pitch class
    '''
    __tablename__='pitches' 

    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(255))
    category=db.Column(db.String(255))
    content=db.Column(db.String(255))
    date_posted=db.Column(db.DateTime,default=datetime.utcnow)
    votes_id=db.Column(db.Integer,db.ForeignKey("votes.id"))
    posted_by=db.Column(db.Integer,db.ForeignKey("users.id"))



class PitchComments(db.Model):
    '''
    model that defines the properties of comments
    '''
    __tablename__='comments'

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255))
    content=db.Column(db.String(255))
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    date_posted=db.Column(db.DateTime,dafault=datetime.utcnow)

    


    
    

