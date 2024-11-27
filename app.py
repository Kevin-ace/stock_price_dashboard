import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# App title
st.title("Basic Stock Price Dashboard")
st.write("Enter a stock ticker to see its real-time price and today's price trend.")

# Input for stock ticker
ticker = st.text_input("Stock Ticker (e.g., AAPL, TSLA, GOOG):", "AAPL")

# Fetch stock data
if ticker:
    try:
        stock_data = yf.Ticker(ticker)
        hist_data = stock_data.history(period="1d", interval="1m")  # 1-minute interval for today

        # Check if historical data exists
        if hist_data.empty:
            st.warning(f"No data found for ticker: {ticker}. It may be invalid or delisted.")
        else:
            # Display stock information with safe field access
            current_price = stock_data.info.get('regularMarketPrice', 'N/A')
            st.subheader(f"Stock: {ticker.upper()}")
            st.write(f"Current Price: **${current_price}**")

            # Plotting the stock price trend
            st.subheader("Today's Price Trend")
            fig, ax = plt.subplots()
            hist_data['Close'].plot(ax=ax, title=f"{ticker.upper()} - 1-Minute Close Prices")
            ax.set_xlabel("Time")
            ax.set_ylabel("Price (USD)")
            st.pyplot(fig)

    except Exception as e:
        st.error(f"An error occurred: {e}")
