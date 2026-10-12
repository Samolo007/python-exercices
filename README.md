# Python Exercices

Ce dépôt contient une série d'exercices Python progressifs, allant du calcul simple et des structures de contrôle jusqu'à l'analyse de données avec pandas, matplotlib et seaborn.

L'objectif est de pratiquer les bases du langage Python puis d'appliquer ces connaissances à des jeux de données réels et pédagogiques.

## Contenu du projet

Le repository est organisé en plusieurs dossiers, chacun correspondant à un exercice ou à un thème précis :

- exercice-01 : calcul de prix TTC, TVA et arrondi
- exercice-02 : statistiques sur des températures et conversions Celsius/Fahrenheit
- exercice-03 : traitement de notes, calcul de moyenne et attribution de mention
- exercice-04 : conditions, saisie utilisateur et année bissextile
- exercice-05 : analyses sur les ventes et le chiffre d'affaires
- exercice-06 : découverte du dataset Titanic avec pandas et seaborn
- exercice-07 : calculs de statistiques sur les passagers du Titanic
- exercice-08 : nettoyage de données, gestion des valeurs manquantes et doublons
- exercice-09 : analyse du taux de survie selon le sexe, la classe et l'âge
- exercice-10 : jointure de données et comparaison par pays d'embarquement
- exercice-11 : exploitation d'un dataset de taxis avec données temporelles
- exercice-12 : visualisations de données et interprétation graphique

## Structure du dépôt

```text
python-exercices/
├── exercice-01/
├── exercice-02/
├── exercice-03/
├── exercice-04/
├── exercice-05/
├── exercice-06/
├── exercice-07/
├── exercice-08/
├── exercice-09/
├── exercice-10/
├── exercice-11/
├── exercice-12/
├── requirements.txt
├── .gitignore
├── README.md
└── .venv/
```

## Prérequis

Python 3 installé sur votre machine, ainsi que les dépendances suivantes :

- pandas
- matplotlib
- seaborn
- jupyter

## Installation

Dans un terminal, à la racine du projet :

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Utilisation

Pour lancer un exercice Python classique :

```bash
python exercice-01/exercice.py
```

Pour ouvrir un notebook Jupyter :

```bash
jupyter notebook
```

Puis sélectionner le notebook correspondant dans l'arborescence du projet.

## Compétences couvertes

Ce projet permet de travailler notamment :

- variables, types et conversions
- opérations mathématiques
- conditions et boucles
- fonctions et modularisation
- structures de données (listes, dictionnaires)
- gestion des erreurs
- analyse de données avec pandas
- visualisation de données avec matplotlib et seaborn
- interprétation de résultats

## Objectif pédagogique

Le but de ce dépôt est d'acquérir progressivement une bonne base en Python et de se familiariser avec l'analyse de données de façon pratique, en réalisant des exercices concrets et variés.
