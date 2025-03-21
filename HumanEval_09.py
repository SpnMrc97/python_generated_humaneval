from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    if not numbers:
        return []

    rolling_max_list = []
    current_max = float('-inf')  # Start with the smallest possible number

    for number in numbers:
        current_max = max(current_max, number)
        rolling_max_list.append(current_max)

    return rolling_max_list
