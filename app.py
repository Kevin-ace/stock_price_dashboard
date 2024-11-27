import streamlit as st
import yfinance as yf
import time
import plotly.graph_objects as go

# App title
st.title("Basic Stock Price Dashboard")
st.write("Enter a stock ticker to see its real-time price and today's price trend.")

# Input for stock ticker
tickers = st.text_input("Enter Stock Tickers (comma-separated, e.g., AAPL, TSLA, GOOG):", "AAPL, TSLA")

# Split and clean ticker list
ticker_list = [t.strip().upper() for t in tickers.split(",")]

# Fetch stock data
for ticker in ticker_list:
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

            # Display additional stock metrics
            day_high = stock_data.info.get('dayHigh', 'N/A')
            day_low = stock_data.info.get('dayLow', 'N/A')
            volume = stock_data.info.get('volume', 'N/A')
            market_cap = stock_data.info.get('marketCap', 'N/A')

            st.write(f"Day's High: **${day_high}**")
            st.write(f"Day's Low: **${day_low}**")
            st.write(f"Volume: **{volume}**")
            st.write(f"Market Cap: **${market_cap}**")

            # Plotting the stock price trend
            st.subheader("Today's Price Trends")
            # Plot using Plotly
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=hist_data.index, y=hist_data['Close'], mode='lines', name='Close Price'))
            fig.update_layout(title=f"{ticker} - 1-Minute Close Prices", xaxis_title="Time", yaxis_title="Price (USD)")
            st.plotly_chart(fig)

    except Exception as e:
        st.error(f"An error occurred: {e}")
