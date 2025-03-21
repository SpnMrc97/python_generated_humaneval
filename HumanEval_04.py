from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        return 0.0  # Return 0.0 if the list is empty to avoid division by zero error
    
    mean_value = sum(numbers) / len(numbers)
    deviations = [abs(x - mean_value) for x in numbers]
    mad = sum(deviations) / len(numbers)
    return mad
