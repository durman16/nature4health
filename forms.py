import psycopg2
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired()])

    password = PasswordField("Password", validators=[DataRequired()])

