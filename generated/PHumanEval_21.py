from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ 
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Parameters:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    List[float]: A list of numbers rescaled to the unit interval [0, 1].

    Example:
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements.")

    min_val = min(numbers)
    max_val = max(numbers)

    if min_val == max_val:
        raise ValueError("All numbers in the list are the same. Cannot rescale to unit interval.")

    return [(x - min_val) / (max_val - min_val) for x in numbers]
