# pages/1_📈_Real_Time_Analysis.py
import streamlit as st
from utils.data_loader import load_stock_data
from utils.ui import render_global_controls
from analysis.patterns import check_golden_cross

# 1. Load the Sidebar Controls
symbol, period = render_global_controls()

st.title(f"📈 Analysis: {symbol}")

# 2. The Main Action Button
if st.button("Run Analysis"):
    with st.spinner(f"Fetching data for {symbol}..."):
        # Get Data
        df = load_stock_data(symbol, period)
    
    if df is not None and not df.empty:
        # Run Pattern Math (Golden Cross)
        is_bullish, df = check_golden_cross(df)
        
        # --- DISPLAY RESULTS ---
        
        # 1. The Verdict
        if is_bullish:
            st.success(f"🚀 **GOLDEN CROSS DETECTED**: The 50-day trend is ABOVE the 200-day trend.")
        else:
            st.info(f"🐻 **No Bullish Pattern**: The 50-day trend is currently BELOW the 200-day trend.")
        
        # 2. Key Stats
        current_price = df['Close'].iloc[-1]
        sma_50 = df['SMA_50'].iloc[-1]
        sma_200 = df['SMA_200'].iloc[-1]
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Current Price", f"${current_price:.2f}")
        col2.metric("50-Day Avg (Fast)", f"${sma_50:.2f}")
        col3.metric("200-Day Avg (Slow)", f"${sma_200:.2f}")
        
        # 3. The Strategy Chart
        st.subheader("Price vs. Moving Averages")
        
        # Filter data for the chart
        chart_data = df[['Close', 'SMA_50', 'SMA_200']]
        
        # Plot with specific colors: White (Price), Blue (50), Red (200)
        st.line_chart(
            chart_data, 
            color=["#FFFFFF", "#0000FF", "#FF0000"]
        )
        st.caption("Legend: White=Price | Blue=50-Day SMA | Red=200-Day SMA")
        
    else:
        st.error(f"Could not find data for {symbol}. Please check the ticker symbol.")
else:
    st.write("Click **Run Analysis** to check for patterns.")