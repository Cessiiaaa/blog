## 🛠️ Technologies utilisées

- **Python 3.10**
- **Django 5.2**
- **Bootstrap 5** — Design responsive
- **Summernote** — Éditeur de texte riche
- **SQLite** — Base de données
- **PythonAnywhere** — Hébergement

## ⚙️ Fonctionnalités

- ✅ Authentification complète (inscription, connexion, déconnexion)
- ✅ Création, modification et suppression d'articles
- ✅ Système de commentaires
- ✅ Recherche par titre et contenu
- ✅ Pagination (6 articles par page)
- ✅ Catégories fixes (Coding, Carrière, Éducation, Tech, Entrepreneuriat, Motivation, Outils)
- ✅ Éditeur de texte riche avec Summernote
- ✅ Protection des pages avec login_required
- ✅ Vérification de l'auteur pour modification et suppression

## 🗄️ Modèles

### Post
| Champ | Type | Description |
|---|---|---|
| titre | CharField | Titre de l'article |
| auteur | ForeignKey | Lié à l'utilisateur Django |
| categorie | CharField | Choix parmi TextChoices |
| description | CharField | Résumé court |
| contenu | TextField | Contenu complet |
| date_creation | DateTimeField | Date automatique |

### Comment
| Champ | Type | Description |
|---|---|---|
| commentaire | TextField | Contenu du commentaire |
| auteur | ForeignKey | Lié à l'utilisateur Django |
| post | ForeignKey | Lié à l'article |

## 🚀 Installation locale

**1. Cloner le dépôt**
```bash
git clone https://github.com/Cessiiaaa/blog.git
cd blog
```

**2. Créer et activer le virtualenv**
```bash
# Windows
python -m venv env
.\env\Scripts\activate

**3. Installer les dépendances**
```bash
pip install django
pip install django-summernote
```

**4. Appliquer les migrations**
```bash
cd blog
py manage.py migrate
```

**5. Créer un superutilisateur**
```bash
py manage.py createsuperuser
```

**6. Lancer le serveur**
```bash
py manage.py runserver
```

Le site est accessible sur [http://127.0.0.1:8000]

## Déploiement sur PythonAnywhere

**1. Cloner le dépôt**
```bash
git clone https://github.com/Cessiiaaa/blog.git
```

**2. Créer le virtualenv**
```bash
mkvirtualenv monenv --python=python3.10
```

**3. Installer les dépendances**
```bash
pip install django django-summernote
```

**4. Appliquer les migrations**
```bash
cd blog/blog
python manage.py migrate
```

**5. Configurer le fichier WSGI**
```python
import os
import sys

path = '/home/ceressia/blog'
if path not in sys.path:
    sys.path.insert(0, path)

path2 = '/home/ceressia/blog/blog'
if path2 not in sys.path:
    sys.path.insert(0, path2)

os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**6. Configurer ALLOWED_HOSTS dans settings.py**
```python
ALLOWED_HOSTS = ['ceressia.pythonanywhere.com']
```

