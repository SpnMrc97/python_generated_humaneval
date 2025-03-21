def sort_third(l: list) -> list:
    # Extract elements at indices divisible by three
    divisible_by_three = [l[i] for i in range(len(l)) if i % 3 == 0]
    
    # Sort these extracted elements
    divisible_by_three_sorted = sorted(divisible_by_three)
    
    # Create a new list to store the result
    result = l[:]
    
    # Reinsert the sorted elements back into their original positions
    j = 0
    for i in range(len(l)):
        if i % 3 == 0:
            result[i] = divisible_by_three_sorted[j]
            j += 1
            
    return result
