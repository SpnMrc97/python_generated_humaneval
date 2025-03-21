def median(l: list) -> float:
    if not l:
        raise ValueError("The list is empty")

    sorted_list = sorted(l)
    n = len(sorted_list)
    mid = n // 2

    if n % 2 == 0:
        # If even, return the average of the two middle numbers
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2.0
    else:
        # If odd, return the middle number
        return sorted_list[mid]
