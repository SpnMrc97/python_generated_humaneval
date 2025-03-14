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

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == []
    assert candidate([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert candidate([4, 3, 2, 1]) == [4, 4, 4, 4]
    assert candidate([3, 2, 3, 100, 3]) == [3, 3, 3, 100, 100]


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(rolling_max)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)