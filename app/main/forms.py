from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required

class PostForm(FlaskForm):

    title = StringField('Post title',validators=[Required()])
    post = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('submit')
        
    
class Comment(FlaskForm):
    content = TextAreaField("Add Comment")
    submit = SubmitField("Add")

class Updateprofile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')