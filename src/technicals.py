import numpy as np
import yfinance as yf

def calculate_rsi(prices, periods=14):
    """Calculate Relative Strength Index."""
    if len(prices) < periods + 1:
        return 50
    
    deltas = np.diff(prices)
    gain = [(x if x > 0 else 0) for x in deltas]
    loss = [(-x if x < 0 else 0) for x in deltas]
    
    avg_gain = np.mean(gain[:periods])
    avg_loss = np.mean(loss[:periods])
    
    if avg_loss == 0:
        return 50
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_technical_indicators(ticker):
    """Calculate technical indicators for a given stock."""
    try:
        stock = yf.Ticker(f"{ticker}.NS")
        data = stock.history(period="1y")
        
        if len(data) < 200:
            return {"SMA Gap (%)": None, "RSI": None}
        
        data["SMA_50"] = data["Close"].rolling(window=50).mean()
        data["SMA_200"] = data["Close"].rolling(window=200).mean()
        
        latest_sma_50 = data["SMA_50"].iloc[-1]
        latest_sma_200 = data["SMA_200"].iloc[-1]
        
        sma_gap = ((latest_sma_50 - latest_sma_200) / latest_sma_200) * 100 if latest_sma_200 else None
        rsi = calculate_rsi(data["Close"].values[-15:])
        
        return {"SMA Gap (%)": sma_gap, "RSI": rsi}
    except:
        return {"SMA Gap (%)": None, "RSI": None}
