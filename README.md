# Projet Student Performance Dashboard

Ce projet fournit un tableau de bord pour analyser la performance des étudiants en fonction de divers facteurs explicatifs. Les facteurs ont été initialement sélectionnés en utilisant un modèle Random Forest pour déterminer l'importance des variables. De plus, pour offrir une flexibilité maximale aux utilisateurs, une fonctionnalité a été ajoutée pour permettre la sélection manuelle des variables à prendre en compte dans l'analyse.

## Caractéristiques principales

1. **Sélection automatique des variables** : Le modèle utilise le Random Forest pour déterminer les variables les plus influentes en termes de performance des étudiants.

2. **Sélection manuelle des variables** : Les utilisateurs ont la liberté d'ajouter ou de retirer des variables du modèle pour voir comment elles influencent la performance.

3. **Ajustement des pondérations** : Une fois les variables sélectionnées, les utilisateurs peuvent ajuster la pondération de chaque variable à l'aide de curseurs, ce qui permet de moduler l'impact de chaque facteur sur l'analyse finale.

## Prérequis

- Installer Docker : Suivez les instructions d'installation [ici](https://docs.docker.com/get-docker/).

## Lancement du projet avec Docker

1. Clonez ce dépôt :
```bash
git clone [lien de votre dépôt]
