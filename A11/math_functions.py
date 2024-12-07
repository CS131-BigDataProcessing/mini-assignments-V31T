def power(base, exponent):
    """Raises a base to the power of an exponent."""
    return base ** exponent

def divide(numerator, denominator):
    """Divides the numerator by the denominator."""
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    return numerator / denominator
