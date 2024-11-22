from src.normalization import normalize

def calculate_score(fundamental, technical):
    """Calculate final investing score."""
    ranges = {
        "P/E Ratio": (15, 45),
        "P/B Ratio": (3, 12),
        "ROE": (15, 35),
        "Debt-to-Equity": (0, 50),
        "Revenue Growth": (5, 20),
        "SMA Gap (%)": (-5, 5),
        "RSI": (30, 70)
    }
    
    weights = {
        "P/E Ratio": 0.15,
        "P/B Ratio": 0.15,
        "ROE": 0.20,
        "Debt-to-Equity": 0.10,
        "Revenue Growth": 0.20,
        "SMA Gap (%)": 0.10,
        "RSI": 0.10
    }
    
    normalized_data = {
        key: normalize(value, *ranges[key], inverse=key in ["P/E Ratio", "P/B Ratio", "Debt-to-Equity"])
        for key, value in {**fundamental, **technical}.items() if key in ranges
    }
    
    total_weight = sum(weights.values())
    score = sum(normalized_data[key] * weights[key] for key in normalized_data) / total_weight
    
    return score, normalized_data
