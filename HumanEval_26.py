from typing import List
from collections import Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Count occurrences of each number
    counts = Counter(numbers)
    
    # Filter the list to include only numbers that appear once
    return [number for number in numbers if counts[number] == 1]
