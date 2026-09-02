from flask import Flask, render_template, url_for


app = Flask(__name__)

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
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)