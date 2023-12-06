# Projet infra réseau 

# Sommaire 

- [Projet infra réseau](#projet-infra-réseau)
- [Sommaire](#sommaire)
- [🎯 Objectif](#-objectif)
- [✅ Checklist](#-checklist)
  - [Bonus](#bonus)
- [🖲️ Technologies et langages utilisés](#️-technologies-et-langages-utilisés)
- [📖 Ressources](#-ressources)


# 🎯 Objectif
Ce projet consiste en la création d'un site disposant d'une page d'accueil, de différentes sections et d'une base de données

Préparation
Créer un répertoire pour le projet qui a cette structure :

```
my-flask-app
   ├── static/
   │   └── css/
   │       └── main.css
   ├── templates/
   │   ├── index.html
   │   └── other.html
   ├── data.py
     ├── main.py
   └── back.py
```

---

# ✅ Checklist

- Mettre en place Flask ✅

```
python -m venv .env_lir2023
.\.env_lir2023\Scripts\activate 
pip install -r requirements.txt
```
---

- Créer la page d'accueil du site ✅

  - [Page d'accueil](/templates/index.html)
---

- Créer 3 autres pages accessibles via des routes (exemple /page2) ✅
  - [Liste membre](/templates/Membres.html)
  - [Contact](/templates/Contact.html)
  - [Info](/templates/Info.html)

---

- Personnaliser le title et le favicon du site (sur la liste de site ouvert) ✅

---

- Styliser le site avec du CSS ✅
  - [Style accueil](static/Index.css)
  - [Style liste membre](static/Membres.css)
  - [Style contact](static/Contact.css)
  - [Style info](static/Info.css)
---

- Mettre en place une base de données sur le serveur qui servira pour le site ✅
  - site en local 
  - db sur une vm
  - connecter les deux
---

## Bonus

- Créer une page pour s'inscrire

- Mettre en place un système de CRUD pour créer, modifier et supprimer un utilisateur

- Utiliser un framework CSS (Bootstrap ou Bulma)

# 🖲️ Technologies et langages utilisés
- Linux
- Web server
- DB

# 📖 Ressources
https://python-adv-web-apps.readthedocs.io/en/latest/flask3.html

https://phoenixnap.com/kb/install-flask

https://kanchanardj.medium.com/forming-database-connection-between-maria-db-and-python-flask-31702c86fd95


