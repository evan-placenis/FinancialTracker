import streamlit as st
from utils.data_loader import load_stock_data
from analysis.patterns import calculate_daily_volatility

st.title("💰 My Portfolio Risk")

# Hardcoded for now, or load from a CSV
my_stocks = ['AAPL', 'GOOGL', 'AMZN', 'MSFT']

st.write(f"Analyzing {len(my_stocks)} holdings...")

for stock in my_stocks:
    data = load_stock_data(stock)
    if data is not None:
        vol = calculate_daily_volatility(data)
        
        # Color code volatility
        if vol > 2.0:
            st.warning(f"**{stock}**: High Volatility ({vol:.2f}%)")
        else:
            st.success(f"**{stock}**: Stable ({vol:.2f}%)")