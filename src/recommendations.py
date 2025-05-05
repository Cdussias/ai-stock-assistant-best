def generate_recommendation(rsi, macd, signal):
    if rsi < 30 and macd > signal:
        return "📈 Consider Buying — RSI is oversold and MACD shows bullish momentum."
    elif rsi > 70 and macd < signal:
        return "📉 Consider Selling — RSI is overbought and MACD shows bearish momentum."
    else:
        return "⏳ Hold — No strong buy or sell signal detected."
