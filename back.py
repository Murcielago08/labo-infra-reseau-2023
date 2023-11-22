from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import mariadb
import sys

app = Flask(__name__)
# app.secret_key = 'votre_clé_secrète'  # Remplacez ceci par une clé secrète sécurisée

# class LoginForm(FlaskForm):
#     username = StringField('Nom d\'utilisateur', validators=[DataRequired()])
#     password = PasswordField('Mot de passe', validators=[DataRequired()])
#     submit = SubmitField('Se connecter')

try:
   conn = mariadb.connect(
      host='127.0.0.1',
      port= 3306,
      user='root',
      password='goldSTAR',
      database='siteDb')
   conn.auto_reconnect = True
except mariadb.Error as e:
   print(f"Error connecting to the database: {e}")
#    sys.exit(1)

@app.route('/')
def accueil():
    return render_template('Index.html')


@app.route('/list_membre')
def List_Membre():

    return render_template('Membres.html')

@app.route('/contact')
def Contact():
    return render_template('Contact.html')

@app.route('/info')
def Info():
    return render_template('Info.html')

    
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         # Ici, vous pouvez vérifier les informations d'authentification et effectuer la connexion
#         # par exemple, vérifier le nom d'utilisateur et le mot de passe
#         # Si les informations sont valides, redirigez l'utilisateur vers une page de succès
#         return redirect(url_for('success'))
#     return render_template('login.html', form=form)

# @app.route('/success')
# def success():
#     return "Connexion réussie"

if __name__ == '__main__':
    app.run(debug=True)
