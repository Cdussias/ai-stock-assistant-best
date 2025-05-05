import yfinance as yf

def get_realtime_data(ticker):
    return yf.download(ticker, period="1d", interval="1m")
