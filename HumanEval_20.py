from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the list to make it easier to find the closest elements
    sorted_numbers = sorted(numbers)
    
    # Initialize variables to store the smallest difference and the closest pair
    min_diff = float('inf')
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    
    # Iterate through the sorted list and find the pair with the smallest difference
    for i in range(len(sorted_numbers) - 1):
        num1 = sorted_numbers[i]
        num2 = sorted_numbers[i + 1]
        diff = num2 - num1
        
        if diff < min_diff:
            min_diff = diff
            closest_pair = (num1, num2)
    
    return closest_pair
