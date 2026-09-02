from flask import Flask, render_template


app = Flask(__name__)

lista_users = ['Rodrigo', 'Rafael', 'Fernanda', 'Alon', 'Flávia']

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/users")
def users():
    return render_template("users.html", lista_users=lista_users)


if __name__ == '__main__':
    app.run(debug=True)