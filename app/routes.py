from flask import render_template, redirect, url_for, flash, request
from app import app, database, bcrypt
from app.forms import FormLogin, FormCreateAccount, FormEditProfile, FormCreatePost, FormEditPost
from app.models import User, Post
from flask_login import login_user, logout_user, current_user, login_required
import secrets
import os
from PIL import Image



@app.route("/")
def home():
    posts = Post.query.order_by(Post.id.desc())
    return render_template("home.html", posts=posts)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/users")
@login_required
def users():
    lista_users = User.query.all()
    return render_template("users.html", lista_users=lista_users)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form_create_account = FormCreateAccount()
    form_login = FormLogin()

    if "btn_submit_login" in request.form and form_login.validate_on_submit():
        user = User.query.filter_by(email=form_login.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form_login.password.data):
            login_user(user, remember=form_login.keep_logged_in.data)
            flash(f"Login successfull for email {form_login.email.data}", "alert-success")
            param_next = request.args.get('next')
            if param_next:
                return redirect(param_next)
            else:
                return redirect(url_for("home"))
        else:
            flash(f"Email ou senha incorretos!", "alert-danger")
    
    if "btn_submit_create_account" in request.form and form_create_account.validate_on_submit():
        pwd_crypt = bcrypt.generate_password_hash(form_create_account.password.data)
        user = User(username=form_create_account.username.data, email=form_create_account.email.data, password=pwd_crypt)
        database.session.add(user)
        database.session.commit()
        flash(f"Account created for email {form_create_account.email.data}", "alert-success")
        return redirect(url_for('login'))

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

@app.route('/post/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = FormCreatePost()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data, author=current_user)
        database.session.add(post)
        database.session.commit()
        flash('Post criado com sucesso', 'alert-success')
        return redirect(url_for('home'))
    return render_template('create_post.html', form=form)


def save_img(img):
    code = secrets.token_hex(8)
    name, ext = os.path.splitext(img.filename)
    filename = name + code + ext
    path = os.path.join(app.root_path, 'static/profile_imgs', filename)
    size = (200, 200)
    img_reduced = Image.open(img)
    img_reduced.thumbnail(size)
    img_reduced.save(path)
    return filename


def update_courses(form):
    course_list = []
    for field in form:
        if "course_" in field.name:
            if field.data:
                course_list.append(field.label.text)
    return ';'.join(course_list)


@app.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = FormEditProfile()
    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.username = form.username.data
        if form.profile_img.data:
            img_name = save_img(form.profile_img.data)
            current_user.profile_img = img_name
        current_user.cursos = update_courses(form)
        database.session.commit()
        flash(f"Perfil atualizado com sucesso.", "alert-success")
        return redirect(url_for('profile'))
    elif request.method == "GET":
        form.email.data = current_user.email
        form.username.data = current_user.username
    profile_img = url_for('static', filename='profile_imgs/{}'.format(current_user.profile_img))
    return render_template('edit_profile.html', profile_img=profile_img, form=form)

@app.route('/post/<post_id>', methods=['GET', 'POST'])
@login_required
def view_post(post_id):
    post = Post.query.get(post_id)
    if current_user == post.author:
        form = FormEditPost()
        if request.method == 'GET':
            form.title.data = post.title
            form.body.data = post.body
        elif form.validate_on_submit():
            post.title = form.title.data
            post.body = form.body.data
            database.session.commit()
            flash('Post atualizado com sucesso', 'alert-success')
            return redirect(url_for('home'))
    else:
        form = None
    return render_template('post.html', post=post, form=form)
