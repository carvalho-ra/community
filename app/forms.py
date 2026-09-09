from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User
from flask_login import current_user


class FormCreateAccount(FlaskForm):
    username = StringField("Usuário", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirm_pwd = PasswordField("Confirmar Senha", validators=[DataRequired(), EqualTo("password")])
    btn_submit_create_account = SubmitField("Criar Conta")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email já cadastrado.')

class FormLogin(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    keep_logged_in = BooleanField("Permanecer conectado")
    btn_submit_login = SubmitField("Entrar")

class FormEditProfile(FlaskForm):
    username = StringField("Usuário", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    btn_submit_edit_profile = SubmitField("Confirmar Edição")
    profile_img = FileField('Atualizar foto de perfil', validators=[FileAllowed(['jpg', 'png'])])
    course_python = BooleanField("Python")
    course_golang = BooleanField("Golang")
    course_Java = BooleanField("Java")
    course_Fullstack = BooleanField("Fullstack")


    def validate_email(self, email):
        if current_user.email != email.data:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email já cadastrado.')

class FormCreatePost(FlaskForm):
    title = StringField("Título", validators=[DataRequired(), Length(2, 100)])
    body = TextAreaField("Escreva seu post aqui...", validators=[DataRequired()])
    btn_submit_post = SubmitField('Criar Post')


class FormEditPost(FlaskForm):
    title = StringField("Título", validators=[DataRequired(), Length(2, 100)])
    body = TextAreaField("Escreva seu post aqui...", validators=[DataRequired()])
    btn_submit_edit_post = SubmitField('Editar Post')
