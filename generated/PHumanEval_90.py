def next_smallest(lst):
    """
    Returns the 2nd smallest element of the list.
    Return None if there is no such element.
    """
    # Convert the list to a set to remove duplicates and sort it
    unique_sorted = sorted(set(lst))

    # Check if there are at least two unique elements
    if len(unique_sorted) < 2:
        return None

    # Return the second smallest element
    return unique_sorted[1]
