# **Projet Student Performance Dashboard**

## **Description**
Ce projet fournit un tableau de bord pour analyser la performance des étudiants en fonction de divers facteurs. Les variables explicatives sont sélectionnées initialement en utilisant la méthode Random Forest. En outre, le tableau de bord offre une flexibilité permettant aux utilisateurs d’ajouter manuellement des variables et d'ajuster leur pondération pour une analyse plus précise.

## **Fonctionnalités**
- **Sélection Automatique des Variables** : Identification des variables les plus pertinentes via Random Forest.
- **Sélection Manuelle des Variables** : Option pour inclure/exclure manuellement des variables dans l'analyse.
- **Ajustement des Ponderations** : Possibilité de modifier la pondération des variables sélectionnées.

## **Prérequis**
- Docker doit être installé. Suivez les instructions d’installation [ici](https://docs.docker.com/get-docker/).

## **Instructions pour Docker**

1. **Clonez le dépôt GitHub**
    ```bash
    git clone https://github.com/MajidAkh/performance_dashboard.git
    ```

2. **Naviguez vers le dossier du projet**
    ```bash
    cd student-performance-dashboard
    ```

3. **Construisez l'image Docker**
    ```bash
    docker build -t student-dashboard .
    ```

4. **Lancez le conteneur Docker**
    ```bash
    docker run -p 8501:8501 student-dashboard
    ```

5. **Accédez au tableau de bord via le navigateur**
    - Ouvrez votre navigateur et visitez `http://localhost:8501`

## **Contact**
Pour plus d'informations ou pour du support, veuillez contacter à [majid.akharaz@gmail.com].

