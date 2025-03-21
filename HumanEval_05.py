from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    if not numbers:  # Handle the empty list case
        return []

    # Start with the first element
    result = [numbers[0]]

    # Iterate through the rest of the list
    for number in numbers[1:]:
        result.append(delimiter)  # Add the delimiter
        result.append(number)     # Add the next number

    return result
