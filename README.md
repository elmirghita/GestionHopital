# 🏥 Gestion D'hopital
Ce projet est une application web dévelopée avec Streamlit et PostgreSQL, destiné à la gestion des factures dans un contexte administratif ou hospitalier. Elle permet d'ajouter, afficher, rechercher, trier et supprimer des factures de maniere simple et intuitive.
# ✨ Fonctionnalité
* Gestion des patients
* Gestion des medecins (departements et specialités)
* Gestion des admissions et des salles d'hospitalisation
* Gestion des consultation médicale
* Gestion des ordonnances
* Gestion de la facturation (factures et ligne de facture)
* Recherche, modification, tri et affichage des données
* Interface web simple et interactive
* Stockage des donnees avec PostgreSQL
# 🔁 Le processus
Le projet a été realisé en plusieurs étapes structurés. Tout d'abord, l'analyse des besoins a permis d'identifier les principales entités du système hospitalier (patients, médecins, admissions, consultation, facturation, etc.).
Ensuite, une base de données relationnelle PostgreSQL et Streamlit, en mettant en place une architecture modulaire et des fonctionnalités CRUD pour chaque module. Enfin, des tests fonctionnels ont été réalisés pour valider le bon fonctionnement de l'application et assurer une expérience utilisateur simple et fiable.
# 🚦 Démarrage du Projet
1. Cloner le dépôt
2. Créer un environnement virtuel: `python -m venv venv`
3. Activer l'environnement virtuel
4. Installer les dependances: `pip install -r requirements.txt`
5. Configuration la base de données dans le fichier `.env`
6. Lancer l'application: `streamlit run app.py`
