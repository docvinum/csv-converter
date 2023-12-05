# CSV Converter & Comparer Tool

## Description

Ce script Python offre deux fonctionnalités principales pour travailler avec des fichiers CSV :
1. **Conversion de Fichiers CSV :** Convertit les fichiers CSV dans un format standardisé (UTF-8 avec une virgule comme séparateur).
2. **Comparaison de Fichiers CSV :** Compare deux fichiers CSV pour identifier les nouvelles entrées, les entrées supprimées et les modifications entre un ancien et un nouveau fichier.

## Fonctionnalités

### Conversion CSV
- Détecte l'encodage d'origine des fichiers CSV.
- Permet à l'utilisateur de spécifier le caractère délimiteur.
- Convertit les fichiers en UTF-8 avec une virgule comme séparateur.

### Comparaison CSV
- Compare deux fichiers CSV en se basant sur une clé unique (première colonne par défaut).
- Identifie et affiche les nouvelles entrées, les entrées supprimées et les entrées modifiées.
- Limite l'affichage des résultats à 10 entrées à la fois avec l'option d'afficher plus d'entrées.

## Prérequis

- Python 3
- Pandas (`pip install pandas`)
- Chardet (`pip install chardet`)

## Utilisation

1. Placez le script `csv_tool.py` dans le répertoire contenant vos fichiers CSV.
2. Exécutez le script avec Python :
   ```bash
   python3 csv_tool.py
   ```
3. Suivez les instructions à l'écran pour choisir entre la conversion et la comparaison de fichiers CSV.
