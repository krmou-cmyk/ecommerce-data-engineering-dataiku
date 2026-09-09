# 🛒 E-commerce Data Engineering Pipeline — Dataiku

Projet Data Engineering end-to-end réalisé avec **Dataiku DSS** à partir du dataset **Olist Brazilian E-Commerce** et de données de taux de change provenant d'une **API REST externe**.

L'objectif est de construire un pipeline de données structuré, contrôlé et orchestré, depuis l'ingestion des données brutes jusqu'à la création de tables analytiques prêtes pour la BI.

## 🏗️ Architecture

Le pipeline suit une architecture en plusieurs couches :

```text
Sources
   │
   ├── Olist CSV
   └── Frankfurter REST API
           │
           ▼
        01_RAW
           │
           ▼
       02_BRONZE
           │
           ▼
       03_SILVER
           │
           ├── 04_DATA_QUALITY
           │
           ▼
        05_GOLD
           │
           ▼
   daily_sales_kpis
```

### RAW
Ingestion des données sources sans transformation métier.

Sources principales :
- Customers
- Orders
- Order Items
- Products
- Payments
- Sellers
- Reviews
- Geolocation
- Category Translation
- Exchange rates API

### BRONZE
Standardisation de l'ingestion et ajout de métadonnées techniques :

- `_source_system`
- `_ingestion_timestamp`
- `_batch_id`

### SILVER
Nettoyage et standardisation :

- typage des colonnes
- nettoyage des chaînes
- normalisation des catégories
- parsing des timestamps
- contrôles de valeurs
- préparation des taux de change quotidiens

### DATA QUALITY
Contrôles de qualité et d'intégrité :

- clés primaires
- clés composites
- valeurs NULL
- unicité
- valeurs numériques positives
- intégrité référentielle PK/FK
- détection des enregistrements orphelins

### GOLD
Construction d'un modèle analytique.

Dimensions :

- `dim_customers`
- `dim_products`
- `dim_date`

Facts :

- `fact_orders`
- `fact_order_items`
- `fact_payments`

Agrégat analytique :

- `daily_sales_kpis`

## 💱 Enrichissement avec une API REST

Les taux de change historiques **BRL → EUR** sont récupérés depuis l'API Frankfurter.

Les données sont ensuite transformées en calendrier quotidien afin de gérer les jours sans publication de taux.

Le chiffre d'affaires est disponible en :

- BRL
- EUR

## 📊 KPIs

La table `daily_sales_kpis` fournit notamment :

- nombre de commandes
- chiffre d'affaires BRL
- chiffre d'affaires EUR
- panier moyen BRL
- panier moyen EUR

## ⚙️ Orchestration

Un scénario Dataiku automatise l'exécution du pipeline :

`BUILD_ECOMMERCE_PIPELINE`

Étapes principales :

1. génération d'un `batch_id`
2. construction automatique des dépendances
3. reconstruction de la couche Gold et des KPIs

Un déclencheur temporel permet également de simuler une exécution quotidienne industrialisée.

## 🛠️ Technologies

- Dataiku DSS
- Python
- Pandas
- REST API
- JSON
- Git / GitHub
- Data Quality
- Data Modeling
- ETL / ELT
- Star Schema

## 📁 Sources de données

**Olist Brazilian E-Commerce Dataset**

Dataset e-commerce brésilien contenant environ 100 000 commandes réalisées entre 2016 et 2018.

**Frankfurter API**

API REST utilisée pour récupérer les taux de change historiques BRL/EUR.

## 🎯 Compétences démontrées

Ce projet met en pratique :

- ingestion multi-source
- conception de pipelines Data Engineering
- architecture RAW / BRONZE / SILVER / GOLD
- consommation d'API REST
- nettoyage et transformation de données
- Data Quality
- contrôle PK/FK
- modélisation dimensionnelle
- orchestration
- gestion des batchs
- versioning Git
- préparation de données pour la BI

## 👤 Auteur

**Karim Oussaidi**

Data / BI / Data Engineering
