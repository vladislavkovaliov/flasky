from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Length(1, 64)]
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )
    remember_me = BooleanField("Keep me logged in")
    submit = SubmitField("Log In")