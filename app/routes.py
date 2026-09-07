from flask import render_template, redirect, url_for, flash, request
from app import app, database, bcrypt
from app.forms import FormLogin, FormCreateAccount, FormEditProfile
from app.models import User, Post
from flask_login import login_user, logout_user, current_user, login_required


lista_users = ['Rodrigo', 'Rafael', 'Fernanda', 'Alon', 'Flávia']

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/users")
@login_required
def users():
    return render_template("users.html", lista_users=lista_users)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form_create_account = FormCreateAccount()
    form_login = FormLogin()

    if "btn_submit_login" in request.form and form_login.validate_on_submit():
        user = User.query.filter_by(email=form_login.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form_login.password.data):
            login_user(user, remember=form_login.keep_logged_in.data)
        else:
            flash(f"Email ou senha incorretos!", "alert_danger")
        flash(f"Login successfull for email {form_login.email.data}", "alert-success")
        param_next = request.args.get('next')
        if param_next:
            return redirect(param_next)
        else:
            return redirect(url_for("home"))
    
    if "btn_submit_create_account" in request.form and form_create_account.validate_on_submit():
        pwd_crypt = bcrypt.generate_password_hash(form_create_account.password.data)
        user = User(username=form_create_account.username.data, email=form_create_account.email.data, password=pwd_crypt)
        database.session.add(user)
        database.session.commit()
        flash(f"Account created for email {form_create_account.email.data}", "alert-success")
        return redirect(url_for('home'))

    return render_template("login.html", form_create_account=form_create_account, form_login=form_login)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash(f"Logout feito com sucesso.", "alert-success")
    return redirect(url_for('home'))

@app.route('/profile')
@login_required
def profile():
    profile_img = url_for('static', filename='profile_imgs/{}'.format(current_user.profile_img))
    return render_template('profile.html', profile_img=profile_img)

@app.route('/post/create')
@login_required
def create_post():
    return render_template('create_post.html')

@app.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = FormEditProfile()
    profile_img = url_for('static', filename='profile_imgs/{}'.format(current_user.profile_img))
    return render_template('edit_profile.html', profile_img=profile_img, form=form)