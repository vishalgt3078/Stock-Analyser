import yfinance as yf
from src.normalization import normalize

def calculate_quarterly_growth(ticker):
    """Calculate quarterly revenue growth."""
    try:
        stock = yf.Ticker(f"{ticker}.NS")
        financials = stock.quarterly_financials
        if financials.empty:
            return None
        
        # Get revenue (Total Revenue)
        revenues = financials.loc['Total Revenue']
        if len(revenues) >= 2:
            latest_revenue = revenues.iloc[0]
            previous_revenue = revenues.iloc[1]
            if previous_revenue != 0:
                growth = ((latest_revenue - previous_revenue) / previous_revenue) * 100
                return growth
        return None
    except:
        return None

def fetch_fundamental_data(ticker):
    """Fetch fundamental data for a given stock."""
    try:
        stock = yf.Ticker(f"{ticker}.NS")
        info = stock.info
        
        # Get quarterly revenue growth
        revenue_growth = calculate_quarterly_growth(ticker)
        
        return {
            "P/E Ratio": info.get("trailingPE"),
            "P/B Ratio": info.get("priceToBook"),
            "ROE": info.get("returnOnEquity", 0) * 100 if info.get("returnOnEquity") else None,
            "Debt-to-Equity": info.get("debtToEquity"),
            "Revenue Growth": revenue_growth
        }
    except:
        return {}
