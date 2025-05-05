import yfinance as yf
import backtrader as bt

class RSIStrategy(bt.Strategy):
    def __init__(self):
        self.rsi = bt.indicators.RSI_SMA(self.data.close, period=14)

    def next(self):
        if not self.position and self.rsi < 30:
            self.buy()
        elif self.position and self.rsi > 70:
            self.sell()

def run_backtest(symbol='AAPL', start='2023-01-01', end='2023-12-31'):
    data = yf.download(symbol, start=start, end=end, auto_adjust=True, progress=False)
    data.reset_index(inplace=True)  # Ensure single-level index
    data.columns = [col.lower() for col in data.columns]  # Lowercase column names
    feed = bt.feeds.PandasData(dataname=data)
    cerebro = bt.Cerebro()
    cerebro.addstrategy(RSIStrategy)
    cerebro.adddata(feed)
    cerebro.run()
    cerebro.plot()
