def common(l1: list, l2: list):
    # Convert lists to sets to find intersection (common elements)
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of both sets
    common_elements = set1.intersection(set2)
    
    # Convert the set of common elements to a sorted list
    return sorted(common_elements)
