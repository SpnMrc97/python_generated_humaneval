def sort_even(l: list) -> list:
    # Extract the elements at even indices
    even_index_elements = [l[i] for i in range(0, len(l), 2)]
    
    # Sort the elements at even indices
    even_index_elements.sort()
    
    # Create a new list to store the result
    result = l[:]
    
    # Replace the elements at even indices with the sorted values
    for i, value in zip(range(0, len(l), 2), even_index_elements):
        result[i] = value
    
    return result
