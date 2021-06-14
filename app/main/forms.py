from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError 

class PitForm(FlaskForm):
    title=StringField('Pitch title', validators=[Required()])
    description=TextAreaField("What would you like to pitch in one minute?", validators=[Required()])
    category=RadioField('Label', choices=[('businesspitch','businesspitch'),('interviewpitch','interviewpitch'),('politicalpitch','politicalpitch'),('religiouspitch','religiouspitch')],validators=[Required()])
    submit=SubmitField('Submit')

    
class PitchCommentsForm(FlaskForm):
    description=TextAreaField('Add comment',validators=[Required()]) 
    Submit=SubmitField() 

class UpvotesForm(FlaskForm):
    Submit=SubmitField()

class DownvotesForm(FlaskForm):
    Submit=SubmitField() 