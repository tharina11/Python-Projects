import pandas as pd

prices = pd.DataFrame({
    "date": ["2025-01-01","2025-01-01","2025-01-02","2025-01-02"],
    "ticker": ["GOOG","MSFT","GOOG","MSFT"],
    "close": [135.1, 410.5, 136.8, 412.2]
})

fundamentals = pd.DataFrame({
    "ticker": ["GOOG","MSFT","NVDA"],
    "sector": ["Technology","Technology","Semiconductors"],
    "pe_ratio": [28.1, 35.4, 72.5]
})
