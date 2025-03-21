def strange_sort_list(lst):
    result = []
    lst_sorted = sorted(lst)
    
    while lst_sorted:
        # Add minimum value
        result.append(lst_sorted.pop(0))
        
        # Add maximum value if there's anything left
        if lst_sorted:
            result.append(lst_sorted.pop(-1))
    
    return result
