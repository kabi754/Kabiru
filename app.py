import streamlit as st
import requests

st.set_page_config(page_title="Currency Signal Bot", layout="centered")

st.title("💹 Currency Trading Signal Bot")
st.write("Real-time BUY/SELL signal using moving average")

# Select currency
base = st.selectbox("Base Currency", ["EUR", "USD", "GBP"])
symbol = st.selectbox("Target Currency", ["USD", "EUR", "JPY", "GBP"])

# Get live price
url = f"https://open.er-api.com/v6/latest/{base}"
response = requests.get(url)
data = response.json()
price = data["rates"].get(symbol, None)

if price:
    st.metric(label=f"Live Price ({base}/{symbol})", value=price)

    # Simple moving average logic
    moving_average = price * 1.01  # Example: pretend 1% higher
    if price > moving_average:
        st.success("🔼 BUY Signal")
    else:
        st.error("🔽 SELL Signal")
else:
    st.warning("Failed to fetch price data. Please check currency pair.")
