#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 17 00:29:42 2025

@author: aishaoyebanji
"""

import streamlit as st
import yfinance as yf
import pandas as pd
import time

st.set_page_config(page_title="Live Stock Dashboard", layout="wide")
st.title("📈 Real-Time Stock Price Dashboard")

ticker_symbol = "MSFT"
ticker = yf.Ticker(ticker_symbol)

placeholder = st.empty()

while True:
    df = ticker.history(period="1d", interval="1m")

    if not df.empty:
        last_price = df["Close"].iloc[-1]
        with placeholder.container():
            st.subheader(f"Live price for **{ticker_symbol}**:")
            st.metric(label="Current Price", value=f"${last_price:.2f}")
            st.line_chart(df["Close"])
    else:
        st.warning("No data available. Try again later.")

    time.sleep(10)  # Refresh every 10 seconds
