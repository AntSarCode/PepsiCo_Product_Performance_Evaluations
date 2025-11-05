# 🥤 PepsiCo Product Performance Evaluations

**Author:** Antony Saragas
**Repository:** [PepsiCo_Product_Performance_Evaluations](https://github.com/AntSarCode/PepsiCo_Product_Performance_Evaluations)
**Last Updated:** November 2025

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.11-informational">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-brightgreen">
  <img alt="Status" src="https://img.shields.io/badge/Status-Active-blue">
</p>

---

## 📘 Overview

This project analyzes **PepsiCo’s product-level performance** across multiple datasets, focusing on sales, profitability, and market distribution trends. The goal is to uncover actionable insights that inform decisions related to **inventory optimization**, **profit margin strategy**, and **product lifecycle management**.

The workflow follows a standard data science pipeline — from raw data ingestion and cleaning to Power BI visualization — with modular, reusable ETL scripts and clear documentation for reproducibility.

---

## 📂 Project Structure

<details>
<summary><b>Click to expand</b></summary>

```text
PepsiCo_Product_Performance_Evaluations/
├─ data/
│  ├─ raw/               # Original CSVs (sales, products, inventory)
│  ├─ processed/         # Cleaned & enriched datasets for BI
│  └─ (interim)/         # Temporary transformations
│
├─ notebooks/
│  ├─ 01_eda_pepsico_sales.ipynb
│  ├─ 02_clean_transform.ipynb
│  ├─ 03_merge_product_stock.ipynb
│  └─ 04_feature_engineering.ipynb
│
├─ scripts/
│  ├─ load_data.py        # Data ingestion & schema validation
│  └─ clean_transform.py  # Core cleaning & transformation logic
│
├─ dashboard/
│  └─ PepsiCo_Sales_Insights.pbix   # Power BI dashboard
│
├─ reports/
│  ├─ dashboard_summary.pdf         # Report overview
│  └─ key_insights.md               # Analytical summaries
│
├─ LICENSE
├─ requirements.txt
└─ README.md
```

</details>

---

### 🔗 Quick Links

* [`data/`](data) – raw → processed data pipeline artifacts
* [`notebooks/`](notebooks) – EDA, cleaning, merge, and feature engineering
* [`scripts/`](scripts) – reusable ETL and transformation scripts
* [`dashboard/`](dashboard) – Power BI report
* [`reports/`](reports) – PDF summaries and insights

---

## 🎯 Objectives

1. **Identify high-performing vs. underperforming products**
   Based on sales volume, margin, and product age.
2. **Detect anomalies or inconsistencies**
   Handle missing values, duplicates, and data quality issues.
3. **Engineer business-focused metrics**
   Profit margin %, stock age, product status, etc.
4. **Deliver interactive executive insights**
   Power BI dashboards built from enriched datasets.

---

## ⚙️ Technical Stack

| Category        | Tools / Libraries                                     |
| --------------- | ----------------------------------------------------- |
| Language        | Python 3.11                                           |
| Data Handling   | `pandas`, `numpy`                                     |
| Visualization   | `matplotlib`, `seaborn`, Power BI                     |
| ETL             | Custom scripts (`load_data.py`, `clean_transform.py`) |
| Environment     | venv / Conda                                          |
| Version Control | Git + GitHub                                          |

---

## 🚀 Workflow Summary

```bash
# 1. Load raw CSVs into DataFrames
python scripts/load_data.py

# 2. Clean, validate, and transform datasets
python scripts/clean_transform.py

# 3. Join product + stock metadata in notebooks
jupyter notebook notebooks/03_merge_product_stock.ipynb

# 4. Export processed data for visualization
# (results saved in /data/processed/)
```

---

## 🧾 Deliverables

* **Cleaned & enriched CSVs** for business intelligence tools.
* **Exploratory data analysis notebooks** documenting insights.
* **Power BI dashboard** summarizing product performance drivers.
* **Automated ETL scripts** for repeatable data processing.

---

## 🧠 Results Snapshot *(optional section placeholder)*

| Metric               | Finding                                    |
| -------------------- | ------------------------------------------ |
| Top SKU Margin       | +32.4% average gross margin                |
| Missing Data Reduced | From 14% to 0.7% after cleaning            |
| Dataset Coverage     | 1,200+ unique products across 5 categories |

---

## 🧾 License

MIT License © 2025 Antony Saragas
See [LICENSE](./LICENSE) for details.

---

## 💬 Contact

**GitHub:** [AntSarCode](https://github.com/AntSarCode)
**Email:** *available upon request*
