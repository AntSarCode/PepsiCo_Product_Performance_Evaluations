import pandas as pd
from load_data import load_stock_data, load_product_data
from pathlib import Path

# Paths
data_dir = Path("../data/raw")
output_dir = Path("../data/processed")
output_dir.mkdir(parents=True, exist_ok=True)

# Load raw data
stock_df = load_stock_data(data_dir / "PEP_stock_data.csv")
product_df = load_product_data(data_dir / "pepsico_products.csv")

# --- CLEAN STOCK DATA ---
# Drop duplicates
stock_df = stock_df.drop_duplicates()

# Round float columns for presentation
float_cols = stock_df.select_dtypes(include='float').columns
stock_df[float_cols] = stock_df[float_cols].round(4)

# Filter to modern data (e.g., post-2000)
stock_df = stock_df[stock_df['Date'].dt.year >= 2000]

# --- CLEAN PRODUCT DATA ---
# Normalize column names
product_df.columns = [col.strip().replace(' ', '_') for col in product_df.columns]

# Fill NA if any
product_df = product_df.fillna("Unknown")

# Create derived features
product_df['Product_Age_2021'] = 2021 - product_df['Year_Launched']
product_df['Is_Active'] = product_df['Status'].apply(lambda x: x.strip().lower() == 'active')

# Export processed versions
stock_df.to_csv(output_dir / "pep_stock_clean.csv", index=False)
product_df.to_csv(output_dir / "pepsico_products_clean.csv", index=False)

print("✔ Data cleaned and saved to /data/processed/")
