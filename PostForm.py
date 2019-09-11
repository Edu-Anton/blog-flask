from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, FileField, DecimalField
from wtforms.validators import Required, Length, NumberRange, InputRequired

class PostForm(FlaskForm):
  title = StringField('title', validators=[InputRequired('Título obligatorio'), Length(min=3, max=100)])
  description = TextAreaField('description', validators=[InputRequired('Nombre obligatorio'), Length(min=3, max=250)])
  url = FileField('url', validators=[InputRequired('Necesitamos una imagen')])
  submit = SubmitField('Salvar')