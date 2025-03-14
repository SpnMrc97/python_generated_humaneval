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

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([2.0, 49.9]) == [0.0, 1.0]
    assert candidate([100.0, 49.9]) == [1.0, 0.0]
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert candidate([2.0, 1.0, 5.0, 3.0, 4.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]
    assert candidate([12.0, 11.0, 15.0, 13.0, 14.0]) == [0.25, 0.0, 1.0, 0.5, 0.75]


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(rescale_to_unit)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)