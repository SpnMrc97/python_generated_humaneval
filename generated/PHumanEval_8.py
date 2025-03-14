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
