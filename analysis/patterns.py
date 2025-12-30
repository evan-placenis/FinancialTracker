# analysis/patterns.py
import pandas as pd

def check_golden_cross(df):
    """
    Returns True if the 50-day SMA is above the 200-day SMA.
    Returns the dataframe with new SMA columns added.
    """
    if len(df) < 200:
        return False, df  # Not enough data
    
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['SMA_200'] = df['Close'].rolling(window=200).mean()
    
    # Check the very last row
    last_row = df.iloc[-1]
    is_bullish = last_row['SMA_50'] > last_row['SMA_200']
    
    return is_bullish, df

def calculate_daily_volatility(df):
    """
    Simple calculation to see how much the price swings.
    """
    df['Daily_Return'] = df['Close'].pct_change()
    volatility = df['Daily_Return'].std() * 100 # In percentage
    return volatility