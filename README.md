Gestion des Produits avec Django et Google Generative AI

Ce projet est une application Django simple qui permet de rechercher des produits en utilisant une intégration avec l'API Google Generative AI pour fournir des réponses basées sur un mot-clé. La base de données utilisée est SQLite.
Fonctionnalités

    Afficher une liste de produits avec leur description et leur prix.
    Rechercher des produits en fonction d'un mot-clé.
    Utiliser Google Generative AI pour analyser et répondre aux requêtes utilisateur.

Technologies utilisées

    Backend : Django 4.x
    Base de données : SQLite
    API externe : Google Generative AI (Gemini)
    Langage : Python 3.8+

Configuration
1. Prérequis

    Python installé sur votre machine.
    Django installé :

pip install django

Bibliothèque google.generativeai installée :

    pip install google-generativeai

2. Cloner le dépôt

Clonez le dépôt Git :

git clone https://github.com/username/nom-du-projet.git
cd nom-du-projet

3. Configuration de l'API Google Generative AI

Ajoutez votre clé API de Google Generative AI dans le fichier source. Remplacez la clé dans views.py :

GEMINI_API_KEY = "VOTRE_CLE_API"

4. Migration de la base de données

Appliquez les migrations pour configurer la base de données SQLite :

python manage.py makemigrations
python manage.py migrate

5. Lancer le serveur

Démarrez le serveur de développement Django :

python manage.py runserver

Ouvrez votre navigateur à l'adresse suivante : http://127.0.0.1:8000.
Structure du projet

    Modèles (models.py) : Définissent les produits avec les champs nom, description, et prix.
    Formulaires (forms.py) : Contient un formulaire pour la recherche par mot-clé.
    Vues (views.py) : Logique de traitement des requêtes utilisateur et intégration avec Google Generative AI.
    Templates : Le fichier HTML produits.html affiche la liste des produits, le formulaire de recherche et les résultats.

Exemple de flux de travail

    L'utilisateur accède à la page principale pour voir une liste de produits.
    Il saisit un mot-clé dans le champ de recherche.
    Le mot-clé est envoyé à Google Generative AI via l'API Gemini.
    Les résultats de l'analyse sont affichés sous forme de texte sur la page.

Dépendances

Installez les dépendances du projet avec la commande :

pip install -r requirements.txt

Exemple de fichier requirements.txt :

django>=4.0
google-generativeai

Limites

    Ce projet utilise une clé API hardcodée dans le fichier views.py. Pour une meilleure sécurité, utilisez des variables d'environnement.
    La réponse de l'API Gemini peut varier en fonction de la qualité des données et du prompt.
