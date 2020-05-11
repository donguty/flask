from wtforms import Form

from wtforms import StringField, PasswordField, validators

class LoginForm(Form):
  username = StringField('Username', [validators.Length(min=4, max=50, message='El username debe contener entre 4-20 letras')])
  password = PasswordField('Password', [validators.DataRequired()])