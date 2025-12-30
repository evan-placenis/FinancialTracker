# utils/data_loader.py
import yfinance as yf
import pandas as pd
import streamlit as st

# We use @st.cache_data so we don't redownload data every time we click a button
@st.cache_data
def load_stock_data(ticker, period="1y"):
    """
    Fetches historical data for a given ticker.
    """
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period=period)
        return df
    except Exception as e:
        return None