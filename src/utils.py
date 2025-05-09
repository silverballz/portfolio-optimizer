# src/utils.py

import pandas as pd

def load_assets(csv_path):
    """
    Load asset data from a CSV file.

    Args:
        csv_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame with columns [Ticker, ExpectedReturn, RiskScore, Price]
    """
    try:
        df = pd.read_csv(csv_path)
        expected_cols = {'Ticker', 'ExpectedReturn(%)', 'RiskScore', 'Price'}
        if not expected_cols.issubset(df.columns):
            missing = expected_cols - set(df.columns)
            raise ValueError(f"Missing columns in CSV: {missing}")

        # Ensure numeric columns are properly typed
        df['ExpectedReturn(%)'] = pd.to_numeric(df['ExpectedReturn(%)'], errors='coerce')
        df['RiskScore'] = pd.to_numeric(df['RiskScore'], errors='coerce')
        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

        # Drop rows with invalid data
        df = df.dropna(subset=['ExpectedReturn(%)', 'RiskScore', 'Price'])

        return df

    except Exception as e:
        print(f"[ERROR] Failed to load assets from {csv_path}: {e}")
        raise
