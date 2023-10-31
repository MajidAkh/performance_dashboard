# Utilisez une image Python officielle comme image de base
FROM python:3.9-slim-buster

# Mettez à jour pip
RUN pip install --upgrade pip

# Répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers de requirements pour les installer
COPY requirements.txt .

# Installez les dépendances
RUN pip install -r requirements.txt

# Copiez tous les autres fichiers du projet dans le conteneur
COPY . .

# Port utilisé par Streamlit
EXPOSE 8501

# Commande pour exécuter l'application Streamlit
CMD ["streamlit", "run", "main.py"]
