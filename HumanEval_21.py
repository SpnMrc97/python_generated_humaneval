from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements.")

    min_val = min(numbers)
    max_val = max(numbers)

    # Avoid division by zero if all numbers are the same
    if min_val == max_val:
        return [0.0 for _ in numbers]

    return [(num - min_val) / (max_val - min_val) for num in numbers]
