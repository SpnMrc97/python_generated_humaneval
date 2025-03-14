def max_element(lst: list) -> int:
    """Return maximum element in the list.

    Args:
        lst (list): A list of integers.

    Returns:
        int: The maximum integer in the list.

    Raises:
        ValueError: If the list is empty.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not lst:
        raise ValueError("The list is empty and has no maximum element.")
    return max(lst)
