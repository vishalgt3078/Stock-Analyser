def normalize(value, min_value, max_value, inverse=False):
    """Normalize a value to a 0-100 scale."""
    if value is None:
        return 50.0
    if max_value == min_value:
        return 50.0
    
    normalized = (value - min_value) / (max_value - min_value)
    normalized = max(0, min(normalized, 1)) * 100
    
    return 100 - normalized if inverse else normalized
