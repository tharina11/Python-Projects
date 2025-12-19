import yfinance as yf
import pandas as pd

# 1. Download Google (GOOG) data
df = yf.download("GOOG", start="2020-01-01", end="2025-01-01")

# --- FIX: Flatten MultiIndex columns (if any) ---
if isinstance(df.columns, pd.MultiIndex):
    df.columns = ['_'.join(col).strip() for col in df.columns.values]

# 2. Reset index so Date becomes a normal column (optional but common)
df = df.reset_index()

# 3. Save to Excel (No MultiIndex → No Error)
df.to_excel("google_stock_data.xlsx", index=False)
print("Google stock data saved successfully!")