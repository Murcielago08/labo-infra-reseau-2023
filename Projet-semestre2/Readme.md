# Projet Ansible et Vagrant

## Sommaire

- [Projet Ansible et Vagrant](#projet-ansible-et-vagrant)
  - [Sommaire](#sommaire)
  - [🎯 Objectif](#-objectif)
  - [Préparation](#préparation)
  - [Machines](#machines)
  - [✅ Checklist](#-checklist)
  - [Bonus](#bonus)
  - [🖲️ Technologies et langages utilisés](#️-technologies-et-langages-utilisés)
  - [📖 Ressources](#-ressources)


## 🎯 Objectif

Ce projet vous fera utiliser le plus possible Ansible avec Vagrant pour déployer et approvisionner des machines virtuelles.

L'inventaire utilisé sera statique, donc il faudra faire attention à bien renseigner les machines à chaque fois.

Le but final d'Ansible est d'être utilisé avec un hyperviseur pour déployer des VM et les provisionner rapidement, mais cela sera fait manuellement dans ce TP.

## Préparation

## Machines

Votre PC hôte sera celui hébergeant les machines. Ca peut être un autre gros PC à vous, ou votre PC portable.

Installez Vagrant sur votre PC hôte.
Installez un hyperviseur compatible avec Vagrant (normalement tous).


## ✅ Checklist

- Paramétrer Vagrant pour créer en une commande trois VM de noms, hostnames et IP différents ✅

- Paramétrer Vagrant pour pouvoir utiliser Ansible pour la provision ✅

- Configurer Vagrant de manière à pouvoir envoyer la clé SSH de l'hôte vers chaque VM

- S'assurer de la connexion SSH à chaque VM

- Configurer les playbooks différents :

  - Playbook database qui devra :

    - Mettre à jour les paquets installés sur la machine

    - Installer PostGreSQL

    - Exécuter en shell une commande pour créer une database,

    - Exécuter en shell une commande pour créer une table et ajouter une entrée (tout au choix)

    - Changer la database pour la rendre disponible au port 7290
      - (Si nécessaire) ajouter une exception dans le pare-feu pour ce port

  - Playbook dbadmin qui devra :

    - Mettre à jour les paquets installés sur la machine

    - Installer PgAdmin

    - Ecrire dans la configuration de PgAdmin pour rendre disponible le site web sur le port 8043
        - (Si nécessaire) ajouter une exception dans le pare-feu pour ce port

- Tester en vous rendant sur l'{adresseIP}:{port} de la machine dbadmin en regardant si votre base est visible [lien du site](http://10.3.1.12:8043)


## Bonus

- Assurer le bon fonctionnement en détruisant les VM puis en relançant Vagrantx

- Variabiliser toutes les variables durs dans les playbooks

- Utiliser des rôles

- Ajouter un playbook pop_smoke qui devra :
  - Mettre à jour les paquets installés sur la machine
  - Ouvrir les ports 92 et 2020 du firewall
  - Installer le paquet nmap
  - Scanner tous les ports ouverts sur le site www.ynov.com
  - Enregistrer les ports considérés comme ouverts dans un fichier
  - Tuer le processus init (0) à la fin de l'exécution

## 🖲️ Technologies et langages utilisés

Vagrant

Machines Virtuelles

Ansible

Playbooks

SSH

YAML

## 📖 Ressources
https://developer.hashicorp.com/vagrant/docs/provisioning/ansible

https://www.pgadmin.org/