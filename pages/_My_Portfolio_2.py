# pages/2_💰_My_Portfolio.py
import streamlit as st
import pandas as pd
from utils.config import MY_STOCKS  # <--- Import the list here
from utils.data_loader import load_stock_data
from analysis.patterns import check_golden_cross

st.title("💰 My Portfolio Overview")
st.write(f"Scanning **{len(MY_STOCKS)}** stocks from your configuration file...")

if st.button("Refresh Portfolio Data"):
    
    # We will store the results in a list to make a nice table later
    report_data = []
    
    # Create a progress bar (looks cool and helpful for loading multiple stocks)
    progress_bar = st.progress(0)
    
    for i, ticker in enumerate(MY_STOCKS):
        # Update progress bar
        progress_bar.progress((i + 1) / len(MY_STOCKS))
        
        # 1. Fetch Data (Defaults to 1 year for trends)
        df = load_stock_data(ticker, period="1y")
        
        if df is not None:
            # 2. Run Analysis
            is_bullish, df = check_golden_cross(df)
            
            # 3. Get Key Metrics
            current_price = df['Close'].iloc[-1]
            prev_price = df['Close'].iloc[-2]
            daily_change = ((current_price - prev_price) / prev_price) * 100
            
            # 4. Add to our report list
            report_data.append({
                "Ticker": ticker,
                "Price": f"${current_price:.2f}",
                "Daily Change": f"{daily_change:.2f}%",
                "Trend": "🟢 Bullish (Golden Cross)" if is_bullish else "🔴 Bearish/Neutral"
            })
    
    # Clear the progress bar when done
    progress_bar.empty()
    
    # 5. Display the Data in a Table
    if report_data:
        st.success("Scan Complete!")
        
        # Convert list to a dataframe for a pretty display
        results_df = pd.DataFrame(report_data)
        
        # Display as an interactive table
        st.dataframe(
            results_df, 
            use_container_width=True,
            hide_index=True
        )
    else:
        st.error("No data found.")

else:
    st.info("Click the button above to pull the latest data for your portfolio.")