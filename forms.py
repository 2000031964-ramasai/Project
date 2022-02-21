from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, validators, RadioField, EmailField
from wtforms.validators import InputRequired


class LoginForm(Form):
    username = StringField('UserName', validators=[InputRequired()])
    password = PasswordField('PassWord', validators=[InputRequired()])
    submit = SubmitField('Login')


class RegisterForm(Form):
    username = StringField('UserName', validators=[InputRequired()])
    password = PasswordField('PassWord', validators=[InputRequired()])
    repassword = PasswordField('Re-PassWord', validators=[InputRequired()])

    phoneno = StringField('phoneno', validators=[InputRequired()])
    email = EmailField('E-mail', validators=[InputRequired(), ])


    submit = SubmitField('Sign up')
