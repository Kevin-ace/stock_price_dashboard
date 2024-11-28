import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# Function to fetch popular stocks
def fetch_popular_stocks():
    try:
        # List of popular tickers (manually curated as yfinance doesn't fetch index components directly)
        popular_tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA", "META", "BRK-B", "V", "JNJ"]
        return popular_tickers
    except Exception as e:
        st.error(f"An error occurred while fetching popular stocks: {e}")
        return ["AAPL", "TSLA", "AMZN", "GOOGL", "MSFT"]  # Default fallback list

# Function to fetch stock data
def fetch_stock_data(ticker):
    try:
        stock_data = yf.Ticker(ticker)
        hist_data = stock_data.history(period="1d", interval="1m")  # 1-minute interval for today
        return stock_data, hist_data
    except Exception as e:
        st.error(f"An error occurred while fetching data for {ticker}: {e}")
        return None, None

# Function to display stock information
def display_stock_info(stock_data):
    current_price = stock_data.info.get('regularMarketPrice', 'N/A')
    day_high = stock_data.info.get('dayHigh', 'N/A')
    day_low = stock_data.info.get('dayLow', 'N/A')
    volume = stock_data.info.get('volume', 'N/A')
    market_cap = stock_data.info.get('marketCap', 'N/A')

    st.write(f"**Current Price:** ${current_price}")
    st.write(f"**Day's High:** ${day_high}")
    st.write(f"**Day's Low:** ${day_low}")
    st.write(f"**Volume:** {volume}")
    st.write(f"**Market Cap:** ${market_cap}")

# Function to plot stock price trends
def plot_stock_trends(hist_data, ticker):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=hist_data.index, y=hist_data['Close'], mode='lines', name='Close Price'))
    fig.update_layout(title=f"{ticker} - 1-Minute Close Prices", xaxis_title="Time", yaxis_title="Price (USD)")
    st.plotly_chart(fig)

# Function to plot candlestick chart
def plot_candlestick_chart(hist_data, ticker):
    fig = go.Figure(data=[
        go.Candlestick(
            x=hist_data.index,
            open=hist_data['Open'],
            high=hist_data['High'],
            low=hist_data['Low'],
            close=hist_data['Close'],
            name='Candlestick'
        )
    ])
    fig.update_layout(title=f"{ticker} - Candlestick Chart", xaxis_title="Time", yaxis_title="Price (USD)")
    st.plotly_chart(fig)

# App title
st.title("Stock Price Dashboard")

# Fetch popular stocks dynamically
st.sidebar.title("Stock Selector")
st.sidebar.write("### Popular Stocks")
popular_stocks = fetch_popular_stocks()

# Sidebar for selecting popular stocks
selected_ticker = st.sidebar.radio("Choose a stock", popular_stocks)

# Search bar for custom stock
st.sidebar.write("### Search for a Stock")
custom_ticker = st.sidebar.text_input("Enter Stock Ticker:", "").strip().upper()

# Determine the stock to display
if custom_ticker:
    stock_to_display = custom_ticker
else:
    stock_to_display = selected_ticker or popular_stocks[0]  # Default to the first stock in the list

# Fetch data for the selected stock
stock_data, hist_data = fetch_stock_data(stock_to_display)

# Display stock data if available
if stock_data is not None and hist_data is not None and not hist_data.empty:
    st.subheader(f"Stock: {stock_to_display}")

    # Display stock information
    st.write("### Stock Information")
    display_stock_info(stock_data)

    # Layout for horizontal charts
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Today's Price Trends")
        plot_stock_trends(hist_data, stock_to_display)
    with col2:
        st.write("### Candlestick Chart")
        plot_candlestick_chart(hist_data, stock_to_display)
else:
    st.warning(f"No data available for {stock_to_display}. It may be invalid or delisted.")
