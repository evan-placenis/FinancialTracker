# app.py
import streamlit as st
from utils.data_loader import load_stock_data
from utils.ui import render_global_controls

# 1. Page Config (Must be the first command)
st.set_page_config(
    page_title="Family Stock Tracker",
    page_icon="🏠",
    layout="wide"
)

# 2. Load the Sidebar Controls
symbol, period = render_global_controls()

st.title("🏠 Family Stock Dashboard")
st.write("Welcome to the command center. Here is the current market pulse.")

# --- MARKET PULSE SECTION (S&P 500) ---
st.markdown("### 🌎 General Market Status (S&P 500)")

col1, col2 = st.columns([1, 3]) # Small column for stats, big for chart

with col1:
    # Fetch data for SPY (S&P 500 ETF)
    spy_data = load_stock_data("SPY", period="1mo")
    
    if spy_data is not None and not spy_data.empty:
        latest_price = spy_data['Close'].iloc[-1]
        start_price = spy_data['Close'].iloc[0]
        profit = latest_price - start_price
        pct_change = (profit / start_price) * 100
        
        # Color code the metric
        st.metric(
            label="SPY Price", 
            value=f"${latest_price:.2f}", 
            delta=f"{profit:.2f} ({pct_change:.1f}%)"
        )
    else:
        st.error("Market data unavailable.")

with col2:
    if spy_data is not None:
        # Green line for market
        st.line_chart(spy_data['Close'], color="#00FF00")

# --- CURRENT SELECTION INFO ---
st.info(f"👉 You are currently set to analyze: **{symbol}** over the last **{period}**. Go to the **Real-Time Analysis** page to see details.")