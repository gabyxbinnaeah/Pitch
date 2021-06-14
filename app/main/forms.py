from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required 

class PitchCommentForm(FlaskForm):
    title=StringField('Pitch title', validators=[Required()])
    content=TextAreaField('Pitch Comment', validators=[Required()])
    submit=SubmitField('Submit')

    
