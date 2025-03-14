def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, this function returns the decimal part
    of the number. The integer part is the largest integer smaller than the given number,
    and the decimal part is the leftover portion, always smaller than 1.

    Parameters:
    number (float): A positive floating point number.

    Returns:
    float: The decimal part of the number.

    Example:
    >>> truncate_number(3.5)
    0.5
    """
    if number < 0:
        raise ValueError("The number must be positive.")

    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part
