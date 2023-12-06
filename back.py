from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import mariadb
import sys
import mysql.connector

app = Flask(__name__)
# app.secret_key = 'votre_clé_secrète'  # Remplacez ceci par une clé secrète sécurisée

# class LoginForm(FlaskForm):
#     username = StringField('Nom d\'utilisateur', validators=[DataRequired()])
#     password = PasswordField('Mot de passe', validators=[DataRequired()])
#     submit = SubmitField('Se connecter')

try:
    conn = mysql.connector.connect(
        host='10.1.1.10',
        port= 3306,
        user='mysql',
        password='test',
        database='siteDb')
    conn.auto_reconnect = True
except mariadb.Error as e:
   print(f"Error connecting to the database: {e}")

# Créer un objet curseur pour exécuter des requêtes SQL
curseur = conn.cursor()

curseur.execute("DROP TABLE IF EXISTS test")

# Exemple : exécuter une requête SQL
curseur.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTO_INCREMENT, user TEXT, password TEXT, description TEXT)")

# Remplacez 'ma_table' par le nom de votre table et ajustez les colonnes et les valeurs selon votre structure
table_name = 'test'
colonne1 = 'id'
colonne2 = 'user'
colonne3 = 'password'
colonne4= 'description'

# Exemple d'insertion de valeurs dans la table
valeurs = [(1, 'John', 'test', 'je suis John'), (2, 'Alice','test', 'je suis Alice'), (3, 'Bob', 'test', 'je suis Bob')]

# Utiliser une requête paramétrée pour éviter les problèmes de sécurité liés aux injections SQL
requete_insertion = f"INSERT INTO {table_name} ({colonne1}, {colonne2}, {colonne3}, {colonne4}) VALUES (%s, %s, %s, %s)"

# Exécuter la requête d'insertion avec les valeurs
curseur.executemany(requete_insertion, valeurs)

# Valider les modifications dans la base de données
conn.commit()

resultats = curseur.fetchall()

# Afficher les résultats
for resultat in resultats:
    print(resultat)

# Fermer le curseur et la connexion
curseur.close()
conn.close()

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
