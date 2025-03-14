from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of input list `numbers`.
    
    Args:
        numbers (List[int]): The list of integers to intersperse.
        delimiter (int): The integer to intersperse between elements.

    Returns:
        List[int]: A new list with the delimiter interspersed between the original elements.
        
    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []
    
    interspersed = []
    for i, number in enumerate(numbers):
        if i > 0:
            interspersed.append(delimiter)
        interspersed.append(number)
    
    return interspersed
