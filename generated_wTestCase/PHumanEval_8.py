from typing import List, Tuple
from functools import reduce
import operator

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, return a tuple consisting of a sum and a product of all the integers in the list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    Tuple[int, int]: A tuple containing the sum and the product of the integers.
    
    Examples:
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    total_sum = sum(numbers)
    total_product = reduce(operator.mul, numbers, 1)
    return total_sum, total_product

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == (0, 1)
    assert candidate([1, 1, 1]) == (3, 1)
    assert candidate([100, 0]) == (100, 0)
    assert candidate([3, 5, 7]) == (3 + 5 + 7, 3 * 5 * 7)
    assert candidate([10]) == (10, 10)


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(sum_product)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)