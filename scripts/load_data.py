import pandas as pd
from pathlib import Path

def load_stock_data(path: str) -> pd.DataFrame:
    """Load and parse PepsiCo stock data CSV."""
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def load_product_data(path: str) -> pd.DataFrame:
    """Load PepsiCo product portfolio CSV."""
    return pd.read_csv(path)

if __name__ == "__main__":
    base_path = Path("../data/raw")
    stock_df = load_stock_data(base_path / "PEP_stock_data.csv")
    product_df = load_product_data(base_path / "pepsico_products.csv")

    print("Stock data preview:")
    print(stock_df.head())
    print("\nProduct data preview:")
    print(product_df.head())
