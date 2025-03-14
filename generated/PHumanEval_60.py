def sum_to_n(n: int) -> int:
    """Calculates the sum of numbers from 1 to n.

    Args:
        n (int): The upper limit of the range to sum.

    Returns:
        int: The sum of numbers from 1 to n.

    Examples:
        >>> sum_to_n(30)
        465
        >>> sum_to_n(100)
        5050
        >>> sum_to_n(5)
        15
        >>> sum_to_n(10)
        55
        >>> sum_to_n(1)
        1
    """
    return n * (n + 1) // 2
