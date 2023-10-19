Description des fichiers fournis:

requirements.txt :
Contient la liste des dépendences Python nécéssaires.
En l'occurence, il spécifie "Flask".

dockerfile :
Contient la description de l'image.
En l'occurence, on par d'une image Python.
On y instal les dépendences contenu dans le requirements.txt via pip.
On expose le port 5000 (port habituelement utilisé par Flask.
Et enfin, il contient la commande de "lancement", la commande qui execute l'appli Python.

python-api-handle-it/app/test_my_module.py
Contient les tests unitaire.

python-api-handle-it/app/main.py
Contient le programme principal

.github/workflows/main.yml
Contient le pipeline d'intégration continue

Ce pipeline se déclenche automatiquement à chaque 'commit' sur le depôt.
___________________________________________________________________________________________

Description des pré-requis:

Seulement avoir un compte Docker Hub pour acceuilir l'image docker generée, car tous les fichiers nécessaires sont dans le Repos.
