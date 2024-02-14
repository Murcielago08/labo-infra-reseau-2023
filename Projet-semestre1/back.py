from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import mysql.connector
from wtforms.fields.simple import TextAreaField


app = Flask(__name__)

# Connexion à la base de données
try:
    conn = mysql.connector.connect(
        host='10.1.1.10',
        port=3306,
        user='mysql',
        password='test',
        database='siteDb')
    conn.auto_reconnect = True
except mysql.connector.Error as e:
    print(f"Error connecting to the database: {e}")

# Créer un objet curseur pour exécuter des requêtes SQL
curseur = conn.cursor()

# Supprimer la table si elle existe
# curseur.execute("DROP TABLE IF EXISTS test")

# Créer la table s'il n'existe pas
curseur.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTO_INCREMENT, user TEXT, password TEXT, description TEXT)")

# Exemple d'insertion de valeurs dans la table
# valeurs = [('John', 'test', 'je suis John'), ('Alice', 'test', 'je suis Alice'), ('Bob', 'test', 'je suis Bob')]

# # Utiliser une requête paramétrée pour éviter les problèmes de sécurité liés aux injections SQL
# requete_insertion = f"INSERT INTO test (user, password, description) VALUES (%s, %s, %s)"

# # Exécuter la requête d'insertion avec les valeurs
# curseur.executemany(requete_insertion, valeurs)

# # Valider les modifications dans la base de données
# conn.commit()

# Clé secrète pour les sessions
app.secret_key = 'oui'

# Définition du formulaire de connexion
class LoginForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Se connecter')

# Route pour la page d'accueil
@app.route('/')
def accueil():
    return render_template('Index.html')

# Route pour la liste des membres
@app.route('/list_membre')
def List_Membre():
    # Rétablir la connexion à la base de données avant d'exécuter la requête SELECT
    conn.reconnect()
    
    # Exécuter la requête SELECT pour récupérer le contenu de la table
    curseur.execute("SELECT user, description FROM test")
    
    # Récupérer toutes les lignes résultantes
    resultats = curseur.fetchall()
    
    # Rendre le template HTML avec les résultats
    return render_template('Membres.html', resultats=resultats)

# Route pour la page de contact
@app.route('/contact')
def Contact():
    return render_template('Contact.html')

# Route pour la page d'information
@app.route('/info')
def Info():
    return render_template('Info.html')

# Définition du formulaire de profil
class ProfileForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Mettre à jour le profil')

# Route pour la page de profil
@app.route('/profil', methods=['GET', 'POST'])
def profil():
    # Récupérer les informations du profil de l'utilisateur depuis la base de données
    curseur.execute("SELECT * FROM test WHERE user = %s", ('utilisateur_test',))
    profil_info = curseur.fetchone()

    # Remplacer 'utilisateur_test' par le nom d'utilisateur actuel de l'utilisateur connecté

    # Créer le formulaire de profil avec les données existantes
    form = ProfileForm(username=profil_info[1], password=profil_info[2], description=profil_info[3])

    if form.validate_on_submit():
        # Récupérer les données mises à jour du formulaire
        new_username = form.username.data
        new_password = form.password.data
        new_description = form.description.data

        # Mettre à jour les informations du profil dans la base de données
        curseur.execute("UPDATE test SET user = %s, password = %s, description = %s WHERE user = %s",
                        (new_username, new_password, new_description, 'utilisateur_test'))
        conn.commit()

    return render_template('profil.html', form=form)

# Route pour le formulaire de connexion
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None

    if form.validate_on_submit():
        # Récupérer les données du formulaire
        username = form.username.data
        password = form.password.data

        # Vérifier si le compte existe
        curseur.execute("SELECT * FROM test WHERE user = %s AND password = %s", (username, password))
        compte_existe = curseur.fetchone()

        if compte_existe:
            # Ajoutez une impression de débogage
            print("Redirection vers le profil")
            return redirect(url_for('profil'))
        else:
            # Ajoutez une impression de débogage
            print("Le compte n'existe pas ou le mot de passe est incorrect.")
            return render_template('login.html', form=form, error="Le compte n'existe pas ou le mot de passe est incorrect.")
        
    # Si l'utilisateur clique sur "S'inscrire", redirigez-le vers la page d'inscription
    if request.args.get('next') == 'inscription':
        return redirect(url_for('inscription'))

    # Passer la variable d'erreur au modèle HTML
    return render_template('login.html', form=form, error=error, redirect_url=request.args.get('next', 'profil'))


# Route pour la page d'inscription
@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        username = request.form['username']
        password = request.form['password']
        description = request.form['description']

        # Insérer l'utilisateur dans la base de données
        curseur.execute("INSERT INTO test (user, password, description) VALUES (%s, %s, %s)", (username, password, description))
        conn.commit()

        # Rediriger vers la page de profil
        return redirect(url_for('profil'))

    return render_template('inscription.html')

# Route pour ajouter un utilisateur (traitement du formulaire)
@app.route('/add_user', methods=['POST'])
def add_user():
    # Récupérer les données du formulaire
    username = request.form['username']
    password = request.form['password']
    description = request.form['description']

    # Insérer l'utilisateur dans la base de données
    curseur.execute("INSERT INTO test (user, password, description) VALUES (%s, %s, %s)", (username, password, description))
    conn.commit()

    return redirect(url_for('login'))

# Démarrage de l'application
if __name__ == '__main__':
    app.run(debug=True)
