def closest_integer(value):
    """
    Convert a string representing a number to the closest integer according to specified rounding rules.

    Args:
    value (str): A string representation of a numeric value.

    Returns:
    int: The closest integer, rounding away from zero if equidistant.

    Examples:
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15
    >>> closest_integer("14.5")
    15
    >>> closest_integer("-14.5")
    -15
    """
    number = float(value)
    if number > 0:
        return int(number + 0.5)
    else:
        return int(number - 0.5)
