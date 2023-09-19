# Utilisation de l'image officielle de Python (choisissez la version appropriée)
FROM python:3.9

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de l'hôte vers le répertoire de travail dans le conteneur
COPY python-api-handle-it/app /app



# Installation des dépendances à partir du fichier requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Lancement de l'application lors du démarrage du conteneur
CMD [ "python", "main.py" ]