from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, FileField, DecimalField
from wtforms.validators import Required, Length, NumberRange, InputRequired

class PostForm(Form):
  title = StringField('Name', validators=[InputRequired('Título obligatorio'), Length(min=3, max=100)])
  description = StringField('Description', validators=[InputRequired('Nombre obligatorio'), Length(min=20, max=250)])
  image = FileField('Imagen', validators=[InputRequired('Necesitamos una imagen')])
  submit = SubmitField('Salvar')