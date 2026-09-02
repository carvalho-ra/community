from flask import Flask, render_template, url_for
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

@app.route("/login")
def login():
    form_create_account = FormCreateAccount()
    form_login = FormLogin()
    return render_template("login.html", form_create_account=form_create_account, form_login=form_login)


if __name__ == '__main__':
    app.run(debug=True)