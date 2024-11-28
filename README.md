# Stock Price Dashboard

## Overview

The Stock Price Dashboard is an interactive web application built using Streamlit and YFinance that allows users to view real-time stock prices, historical price trends, and candlestick charts. Users can select from a list of popular stocks or search for a stock by ticker symbol to view detailed stock information and visualizations.

You can check its preview on; https://kevin-ace-stock-price-dashboard-app-i7nkd9.streamlit.app/

This project provides a user-friendly interface with:

- Real-time stock data.
- Interactive charts (line and candlestick).
- Stock information such as price, volume, market cap, and high/low of the day.
- A sidebar with popular stocks and a custom search bar to find any stock.

## Features

1. **Real-Time Stock Price Information**: Display the current stock price, day's high, day's low, volume, and market cap.
2. **Historical Price Trends**: Interactive line chart showing the stock's 1-minute price changes for the day.
3. **Candlestick Chart**: Provides a detailed view of stock price fluctuations with open, high, low, and close values.
4. **Popular Stock List**: A sidebar that shows a list of popular stocks, and a user can select from these to display charts.
5. **Stock Search**: A search bar allows users to enter a custom ticker symbol to fetch data and charts.
6. **Dynamic Updates**: The app fetches data from the YFinance API and updates charts dynamically for each stock selected.

## Installation
### Prerequisites
- Python 3.7 or higher
- Install the necessary Python libraries via requirements.txt.

1. Clone the repository
```bash
git clone https://github.com/your-username/stock-price-dashboard.git
cd stock-price-dashboard
```
2. Create a Virtual Environment
It's recommended to use a virtual environment for managing dependencies.
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
```
3. Install Required Libraries
Use the requirements.txt to install the necessary packages:
```bash
pip install -r requirements.txt
```

Here is the content of requirements.txt:
```
streamlit
yfinance
plotly
```

4. Run the App
To start the app locally:
```bash
streamlit run app.py
```

5. Open the app in your browser
Once the app starts, open the URL provided by Streamlit in your browser (usually http://localhost:8501).

## Usage
### Sidebar Options:
- **Choose a stock**: A radio button that lets you select from a list of popular stocks.
- **Search for a stock**: A text input box where you can type the ticker symbol (e.g., AAPL, GOOGL, etc.) to get stock information and charts for any stock of your choice.

### Main Area:
- **Stock Information**: Displays the current stock price, day’s high, day’s low, volume, and market cap.
- **Price Trends**: A line chart showing the stock’s close prices over a 1-minute interval.
- **Candlestick Chart**: Displays the stock's price movement in a candlestick format for a more detailed view.

### Popular Stocks List:
The app includes a list of popular stocks that are updated based on a manually curated list. You can select one of these popular stocks from the sidebar for quick access to its details.

## How it Works
### Fetching Stock Data:
The app uses the YFinance API to fetch real-time stock information. You can retrieve stock data for any ticker symbol by using the yf.Ticker(ticker) function and historical data by using the .history() method with the desired time period and interval.

### Plotting with Plotly:
The app uses Plotly to plot stock price trends:

1. **Line Chart**: A simple line chart showing stock closing prices over a specified interval (1-minute).
2. **Candlestick Chart**: A detailed view of stock price movement with open, high, low, and close values displayed for each minute.

### Streamlit Layout:
- **Sidebar**: Allows the user to select a stock or input a custom ticker symbol to fetch data.
- **Main Area**: Displays the stock information and charts side-by-side using Streamlit’s column layout.


## Contributing
Feel free to fork this project, submit issues, or make pull requests. If you'd like to contribute, please:

1. Fork the repository.
2. Create a feature branch
```bash
git checkout -b feature-name
```
3. Commit your changes
```bash
git commit -m 'Add new feature'
```
4. Push to the branch 
```bash
git push origin feature-name
```
Open a pull request.
