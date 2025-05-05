import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from technical_analysis import add_indicators
from recommendations import generate_recommendation
from realtime_data import get_realtime_data
from backtest import run_backtest

st.set_page_config(page_title="🚀 Advanced AI Stock Assistant", layout="wide")
st.title("📈 AI Stock Assistant")

ticker = st.text_input("Enter Stock Ticker", "AAPL")
col1, col2 = st.columns(2)
start = col1.date_input("Start Date", pd.to_datetime("2023-01-01"))
end = col2.date_input("End Date", pd.to_datetime("2023-12-31"))

if st.button("📉 Analyze Stock"):
    data = get_realtime_data(ticker)
    data = add_indicators(data)
    st.line_chart(data['Close'], use_container_width=True)
    st.line_chart(data[['RSI']], use_container_width=True)
    st.line_chart(data[['MACD', 'Signal']], use_container_width=True)
    rsi_latest = data['RSI'].dropna().iloc[-1]
    macd_latest = data['MACD'].dropna().iloc[-1]
    signal_latest = data['Signal'].dropna().iloc[-1]
    recommendation = generate_recommendation(rsi_latest, macd_latest, signal_latest)
    st.info(recommendation)

if st.button("📊 Run Backtest"):
    st.write("Launching backtest window...")
    run_backtest(ticker, str(start), str(end))

st.markdown("---")
st.subheader("💬 Ask AI About Stocks (Coming Soon...)")
st.warning("Chatbot module will be integrated shortly using OpenAI.")
