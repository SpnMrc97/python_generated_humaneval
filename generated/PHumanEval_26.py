from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers with duplicates removed, keeping the original order of first occurrences.

    Examples:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    # Dictionary to keep track of the occurrence count of each number
    occurrence_count = {}
    
    # List to store the result
    result = []
    
    # First pass to count occurrences of each number
    for number in numbers:
        if number in occurrence_count:
            occurrence_count[number] += 1
        else:
            occurrence_count[number] = 1
    
    # Second pass to construct the result list with only unique numbers
    for number in numbers:
        if occurrence_count[number] == 1:
            result.append(number)
    
    return result
