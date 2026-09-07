from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User


class FormCreateAccount(FlaskForm):
    username = StringField("User", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(6, 20)])
    confirm_pwd = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    btn_submit_create_account = SubmitField("Create account")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email já cadastrado.')

class FormLogin(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(6, 20)])
    keep_logged_in = BooleanField("Keep Logged In")
    btn_submit_login = SubmitField("Login")
