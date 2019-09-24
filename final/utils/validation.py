# Validation utilities

def ensure_positive_float(val):
    if type(val) is float or type(val) is int:
        if float(val) >= 0:
            return float(val)
    
