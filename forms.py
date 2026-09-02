from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class FormCreateAccount(FlaskForm):
    username = StringField("User", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(6, 20)])
    confirm_pwd = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    btn_submit_create_account = SubmitField("Create account")


class FormLogin(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(6, 20)])
    keep_logged_in = BooleanField("Keep Logged In")
    btn_submit_login = SubmitField("Login")
