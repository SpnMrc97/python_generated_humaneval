def median(l: list) -> float:
    """Return median of elements in the list l."""
    if not l:
        raise ValueError("The list is empty")
    
    sorted_list = sorted(l)
    n = len(sorted_list)
    mid = n // 2

    # If the number of elements is odd, return the middle one
    if n % 2 == 1:
        return float(sorted_list[mid])
    # If the number of elements is even, return the average of the middle two
    else:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2.0
