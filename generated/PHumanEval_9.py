from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of the rolling maximum element found until the given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    rolling_max_list = []
    current_max = float('-inf')

    for number in numbers:
        current_max = max(current_max, number)
        rolling_max_list.append(current_max)

    return rolling_max_list
