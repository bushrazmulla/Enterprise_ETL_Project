# 🚀 Enterprise Multi-Source ETL Pipeline using Python & MySQL

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-green?logo=pandas)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?logo=mysql)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

# 📌 Project Overview

This project demonstrates an **end-to-end Enterprise ETL (Extract, Transform, Load) Pipeline** built using **Python, Pandas, SQLAlchemy, and MySQL**.

The pipeline extracts data from multiple business sources, performs comprehensive data cleaning and transformation, validates data quality, derives business metrics, and loads the final analytical dataset into a relational database.

The resulting dataset is designed to support:

- Business Intelligence (BI)
- Reporting & Dashboards
- Data Analytics
- Machine Learning
- Generative AI / RAG Applications

---

# 🎯 Business Problem

Organizations receive data from multiple operational systems such as:

- Sales Systems
- Customer Management Systems (CRM)
- Product Catalogs

Raw business data is often:

- Inconsistent
- Duplicate
- Missing important values
- Stored across multiple files

Such data cannot be directly used for analytics or AI.

This ETL pipeline transforms raw business data into a clean, structured, and reliable dataset ready for downstream applications.

---

# 🏗️ ETL Architecture

```text
             Raw Data Sources
      ├── sales.csv
      ├── customers.csv
      └── products.csv
              │
              ▼
          EXTRACT
              │
              ▼
         TRANSFORM
      • Remove Duplicates
      • Handle Missing Values
      • Standardize Dates
      • Merge Datasets
      • Calculate Revenue
      • Validate Data
              │
              ▼
            LOAD
              │
              ▼
       MySQL Database
              │
              ▼
 Business Intelligence / SQL / AI / RAG
```
'''
⚙️ Technologies Used
| Technology | Purpose                        |
| ---------- | ------------------------------ |
| Python     | ETL Pipeline Development       |
| Pandas     | Data Cleaning & Transformation |
| SQLAlchemy | Database Connectivity          |
| MySQL      | Relational Database            |
| PyMySQL    | MySQL Driver                   |
| SQL        | Data Retrieval & Analysis      |


## 📂 Project Structure

```text
Enterprise_ETL_Project/
│
├── data/
│   └── raw/
│       ├── sales.csv
│       ├── customers.csv
│       └── products.csv
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── config.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 1️⃣ Extract

Data is extracted from three independent business sources:

- Sales Data
- Customer Data
- Product Data

The extraction layer converts raw CSV files into Pandas DataFrames.

## 2️⃣ Transform

Several business transformations are applied during the transformation phase.

### ✔ Duplicate Removal

Removes duplicate transactional records to prevent inaccurate reporting.

### ✔ Missing Value Handling
Removes duplicate transactional records to prevent inaccurate reporting.

✔ Missing Value Handling
| Column        | Rule                   |
| ------------- | ---------------------- |
| Quantity      | Replace with 1         |
| Customer Name | Replace with "Unknown" |
| Product Price | Replace with 0         |

###✔ Date Standardization
```text
Converts multiple date formats into a consistent format.
Example:
07/03/2026

↓

2026-07-03
```
###✔ Dataset Integration

Customer, Sales, and Product datasets are merged using:

- CustomerID
- ProductID

This creates a unified analytical dataset.

This creates a unified analytical dataset.

###✔ Feature Engineering

A new business metric is derived.

```text
Revenue = Quantity × Price
```
###✔ Data Validation

Validation checks include:

Missing Product Prices
Missing IDs
Invalid Revenue
Data Integrity
##3️⃣ Load

The transformed dataset is loaded into MySQL using SQLAlchemy.

The final table:

sales_report

can be queried using SQL and consumed by downstream applications.

# 📊 Sample Output
| OrderID | CustomerName | Product  | Revenue |
| ------- | ------------ | -------- | ------: |
| 1001    | Bushra       | Laptop   |  120000 |
| 1002    | Ali          | Mouse    |     700 |
| 1003    | Bushra       | Keyboard |    4500 |

# 💡 Key Features
✅ Multi-source Data Extraction
✅ Modular ETL Architecture
✅ Data Cleaning
✅ Missing Value Handling
✅ Duplicate Removal
✅ Data Validation
✅ Revenue Calculation
✅ MySQL Integration
✅ SQL Ready

# 🎓 Key Learnings
This project strengthened my understanding of:
ETL Architecture
Data Engineering Concepts
SQL
Relational Databases
Data Cleaning
Feature Engineering
Data Validation
Database Loading
Enterprise Data Pipelines

# 🤖 ETL for Generative AI
```text

Large Language Models require clean and structured data.

This ETL pipeline prepares enterprise data that can later be:

Raw Data

↓

ETL Pipeline

↓

MySQL

↓

Embeddings

↓

Vector Database

↓

Retriever

↓

Large Language Model (LLM)
```
