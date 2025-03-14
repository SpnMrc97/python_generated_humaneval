def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting.
    Sort the array in ascending order if the sum of the first and last index values is odd,
    or sort it in descending order if the sum is even.

    Note:
    * Do not change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    if not array:
        return []

    first_value = array[0]
    last_value = array[-1]
    sum_first_last = first_value + last_value

    if sum_first_last % 2 == 0:
        # Sort in descending order
        return sorted(array, reverse=True)
    else:
        # Sort in ascending order
        return sorted(array)

def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([]) == [], "Error"
    assert candidate([5]) == [5], "Error"
    assert candidate([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5], "Error"
    assert candidate([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0], "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([2, 1]) == [1, 2], "Error"
    assert candidate([15, 42, 87, 32 ,11, 0]) == [0, 11, 15, 32, 42, 87], "Error"
    assert candidate([21, 14, 23, 11]) == [23, 21, 14, 11], "Error"


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(sort_array)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)