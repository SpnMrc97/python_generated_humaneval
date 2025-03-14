from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """Calculate the Mean Absolute Deviation (MAD) of a list of numbers.
    
    The MAD is the average of the absolute differences between each number
    and the mean of the list.

    Args:
        numbers (List[float]): A list of floating-point numbers.
    
    Returns:
        float: The mean absolute deviation of the numbers.
    
    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    
    mean_value = sum(numbers) / len(numbers)
    deviations = [abs(x - mean_value) for x in numbers]
    mad = sum(deviations) / len(numbers)
    return mad

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert abs(candidate([1.0, 2.0, 3.0]) - 2.0/3.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0/5.0) < 1e-6


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(mean_absolute_deviation)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)