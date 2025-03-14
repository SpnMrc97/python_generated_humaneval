def sort_even(l: list) -> list:
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal
    to the values of the even indices of l, but sorted.
    """
    # Extract even-indexed elements
    even_indexed_elements = [l[i] for i in range(len(l)) if i % 2 == 0]
    
    # Sort the even-indexed elements
    even_indexed_elements_sorted = sorted(even_indexed_elements)
    
    # Construct the new list with sorted even indices
    result = l[:]  # Make a copy of the original list
    even_index = 0
    
    for i in range(len(result)):
        if i % 2 == 0:
            result[i] = even_indexed_elements_sorted[even_index]
            even_index += 1
    
    return result
