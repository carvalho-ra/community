from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormCreateAccount, FormLogin


app = Flask(__name__)

app.config["SECRET_KEY"] = "028d82684689544411b57f7562dd2b41"


lista_users = ['Rodrigo', 'Rafael', 'Fernanda', 'Alon', 'Flávia']

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/users")
def users():
    return render_template("users.html", lista_users=lista_users)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form_create_account = FormCreateAccount()
    form_login = FormLogin()

    if "btn_submit_login" in request.form and form_login.validate_on_submit():
        flash(f"Login successfull for email {form_login.email.data}", "alert-success")
        return redirect(url_for("home"))
    
    if "btn_submit_create_account" in request.form and form_create_account.validate_on_submit():
        flash(f"Account created for email {form_create_account.email.data}", "alert-success")
        return redirect(url_for('home'))

    return render_template("login.html", form_create_account=form_create_account, form_login=form_login)


if __name__ == '__main__':
    app.run(debug=True)