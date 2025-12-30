# utils/ui.py
import streamlit as st
from utils.config import MY_STOCKS # Import the list

def render_global_controls():
    """
    Renders the Ticker and Time Period inputs in the Sidebar.
    Returns: (symbol, period)
    """
    
    if 'symbol' not in st.session_state:
        st.session_state['symbol'] = "AAPL"
    if 'time_period' not in st.session_state:
        st.session_state['time_period'] = "1y"

    with st.sidebar:
        st.header("⚙️ Dashboard Controls")
        
        # --- NEW FEATURE: PORTFOLIO QUICK SELECT ---
        # We add "Custom" to the list so he can still type other stocks
        options = ["Type Custom..."] + MY_STOCKS
        
        selection = st.selectbox("Select from Portfolio:", options)
        
        # If he selects a stock, update the symbol automatically
        if selection != "Type Custom...":
            st.session_state['symbol'] = selection
        
        # --- STANDARD CONTROLS ---
        # Show the text box (it will auto-fill if he picked from the dropdown)
        current_symbol = st.session_state['symbol']
        new_symbol = st.text_input("Ticker Symbol", value=current_symbol).upper()
        st.session_state['symbol'] = new_symbol
        
        # Time Period
        periods = ["1mo", "3mo", "6mo", "1y", "2y", "5y"]
        default_index = 3
        if st.session_state['time_period'] in periods:
            default_index = periods.index(st.session_state['time_period'])
            
        new_period = st.selectbox("Time Period", periods, index=default_index)
        st.session_state['time_period'] = new_period
        
        st.markdown("---")
        
    return new_symbol, new_period