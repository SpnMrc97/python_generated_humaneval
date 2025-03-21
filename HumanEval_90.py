def next_smallest(lst):
    # Convert the list to a set to remove duplicates
    unique_elements = set(lst)
    
    # If there are fewer than 2 unique elements, return None
    if len(unique_elements) < 2:
        return None
    
    # Convert the set back to a sorted list
    sorted_elements = sorted(unique_elements)
    
    # Return the second smallest element
    return sorted_elements[1]
