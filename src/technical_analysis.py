import ta

def add_indicators(df):
    df['Close'] = df['Close'].squeeze()  # Ensure 'Close' is 1D
    rsi = ta.momentum.RSIIndicator(close=df['Close'])
    macd = ta.trend.MACD(close=df['Close'])
    df['RSI'] = rsi.rsi()
    df['MACD'] = macd.macd()
    df['Signal'] = macd.macd_signal()
    return df
