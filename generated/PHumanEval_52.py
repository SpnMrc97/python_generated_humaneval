def below_threshold(l: list, t: int) -> bool:
    """Return True if all numbers in the list l are below threshold t.

    Args:
        l (list): A list of integers.
        t (int): The threshold integer.

    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.

    Examples:
        >>> below_threshold([1, 2, 4, 10], 100)
        True
        >>> below_threshold([1, 20, 4, 10], 5)
        False
    """
    return all(x < t for x in l)
