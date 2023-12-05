# CSV UTF-8 Converter

## Description du Projet

Ce projet propose un script Python pratique conçu pour simplifier le processus de manipulation des fichiers CSV, en ciblant spécifiquement l'encodage des fichiers et leur format de séparation. Il détecte automatiquement l'encodage et le caractère de séparation des fichiers CSV dans le répertoire courant et offre la possibilité de les convertir en UTF-8 avec une virgule comme séparateur. Cette fonctionnalité est utile pour l'intégration de données, le nettoyage des données, et la collaboration.

## Fonctionnalités Clés

- **Détection Automatique :** Identifie l'encodage actuel et le caractère de séparation de chaque fichier CSV.
- **Conversion Flexible :** Convertit des fichiers spécifiques ou tous les fichiers CSV du répertoire en UTF-8 avec une virgule comme séparateur.
- **Facilité d'Utilisation :** Accessible à un large éventail d'utilisateurs, y compris ceux qui travaillent dans des domaines non techniques.

## Utilisation

1. Placez `convert_csv.py` dans le répertoire contenant vos fichiers CSV.
2. Exécutez le script avec Python :
   ```bash
   python3 convert_csv.py
   ```
3. Suivez les instructions à l'écran pour sélectionner les fichiers à convertir.

## Dépendances

- Python 3
- Module `chardet` (installé via `pip install chardet`)

## Cas d'Utilisation

- **Intégration de Données :** Unifie les formats de fichiers CSV pour l'importation dans des bases de données ou des systèmes d'analyse.
- **Nettoyage des Données :** Assure la cohérence des formats de fichier CSV pour faciliter le nettoyage et l'analyse.
- **Collaboration et Partage :** Convertit les fichiers pour garantir la compatibilité lors du partage avec des collègues ou des parties prenantes.

## Technologies Utilisées

- **Python :** Langage de script polyvalent pour le traitement de fichiers et l'automatisation des tâches.
- **Chardet :** Bibliothèque Python pour détecter l'encodage des fichiers.

## Auteur


## Licence

Ce projet est sous licence X. Voir le fichier `LICENSE` pour plus d'informations.
