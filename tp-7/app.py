from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# check if user exists
def user_exists(username):
    with open('users.json', 'r') as f:
        users = json.load(f)
        return username in users


def check_credentials(username, password):
    with open('users.json', 'r') as f:
        users = json.load(f)
        return users.get(username) == password


@app.route('/')
def home():
    return 'Bienvenue !'

# sign up page route
@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if user_exists(username):
            return 'L\'utilisateur existe déjà. Choisissez un autre nom d\'utilisateur.'
        with open('users.json', 'r') as f:
            users = json.load(f)
        users[username] = password
        with open('users.json', 'w') as f:
            json.dump(users, f)

        return redirect(url_for('connexion'))

    return render_template('inscription.html')

# connexion page route
@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # check identification
        if check_credentials(username, password):
            return f'Bienvenue, {username} !.'
        else:
            return 'Nom d\'utilisateur ou mot de passe incorrect.'

    return render_template('connexion.html')

if __name__ == '__main__':
    app.run(debug=True)
