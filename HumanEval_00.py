from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Check consecutive pairs for the threshold condition
    for i in range(len(sorted_numbers) - 1):
        if abs(sorted_numbers[i] - sorted_numbers[i + 1]) < threshold:
            return True
    
    return False
