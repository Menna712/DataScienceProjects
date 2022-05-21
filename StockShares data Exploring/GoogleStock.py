#pip install streamlit
import yfinance as yf
import streamlit as st
import pandas as pd
st.write("""
# Simple Stock Price App
explore the stock price and volume of Google
""")
tickerSymbol='GOOGL'
tickerData=yf.Ticker(tickerSymbol)
tickerDF=tickerData.history(period='1d',start='2012-5-21',end='2022-5-21')
st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)

###write in terminal 
# streamlit run GoogleStock.py
###to view the web app