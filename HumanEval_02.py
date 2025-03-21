import math

def truncate_number(number: float) -> float:
    # Use math.modf to separate the fractional and integer parts
    fractional_part, integer_part = math.modf(number)
    return fractional_part
