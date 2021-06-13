from flask_wtf import FlaskForm
from wtforms import StringField,Textarea,SubmitField
from wtf.validators import Required 

class PitchCommentForm(FlaskForm):
    title=StringField('Pitch Comments', validators=[required])
    