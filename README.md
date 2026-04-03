PreSkool - Système de Gestion Scolaire



Instructions d'Installation :

Suivez ces étapes pour configurer le projet localement après avoir extrait le dossier compressé.

1. Prérequis :

    Python 3.10 ou plus récent installé.

    Un gestionnaire de paquets (pip).

2. Configuration de l'Environnement :

Ouvrez votre terminal dans le dossier du projet :


# Création de l'environnement virtuel
python -m venv venv

# Activation de l'environnement
# Sur Windows :
venv\Scripts\activate
# Sur Mac/Linux :
source venv/bin/activate

3. Installation des Dépendances


 pip install -r requirements.txt


4. Initialisation de la Base de Données (SQLite)


python manage.py makemigrations
python manage.py migrate

4. Initialisation de la Base de Données (SQLite)
Bash

python manage.py makemigrations
python manage.py migrate

Accédez à l'application via : http://127.0.0.1:8000/

Identifiants de Test :

Pour explorer toutes les fonctionnalités (y compris l'administration), utilisez les comptes suivants :
| Rôle | Nom d'utilisateur / Email | Mot de passe |
| :--- | :--- | :--- |
| **Administrateur** | `ayaelissaoui` | `aya123` |
| **Enseignant** | `chorouk@user.com` | `chorouk123` |
| **Étudiant** | `ahssaini@user.com` | `hiba123` |

    Note : Accès à l'interface d'administration Django sur http://127.0.0.1:8000/admin/.


## 🎬 Démonstration Vidéo

Vous pouvez visionner une présentation complète des fonctionnalités (Dashboard, Ajout Étudiant, Gestion Départements) via le lien ci-dessous :

👉 **[Visionner la Démo Vidéo du Projet PreSkool](https://1drv.ms/v/c/292b2e52cf235255/IQBbJrDnM-6ER4NFAfbw-qjJAcijWRBMXG__w2FScuvFPm0?e=9qazp2)**

> ⚠️ **Note importante sur la qualité :** Le lecteur OneDrive peut afficher une qualité réduite par défaut. Pour une lisibilité optimale du code et des graphiques IDAI, veuillez régler la qualité sur **1080p HD** via l'icône d'engrenage (paramètres) du lecteur.







Technologies Utilisées :

    Backend : Python & Django 6.0

    Base de données : SQLite 3

    Frontend : HTML5, CSS3 (Bootstrap), Feather Icons


Retrouvez l'intégrité du code ici : "https://github.com/ELISSAOUIAYA/PFM_PreSkool" 
