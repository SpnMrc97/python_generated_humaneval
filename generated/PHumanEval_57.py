def monotonic(l: list) -> bool:
    """Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of comparable elements.

    Returns:
        bool: True if the list is monotonic, False otherwise.

    Examples:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """
    if not l:
        return True

    increasing = decreasing = True

    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            decreasing = False
        elif l[i] < l[i - 1]:
            increasing = False

    return increasing or decreasing
