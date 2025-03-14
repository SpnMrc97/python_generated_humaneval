def median(l: list) -> float:
    """Return median of elements in the list l."""
    if not l:
        raise ValueError("The list is empty")
    
    sorted_list = sorted(l)
    n = len(sorted_list)
    mid = n // 2

    # If the number of elements is odd, return the middle one
    if n % 2 == 1:
        return float(sorted_list[mid])
    # If the number of elements is even, return the average of the middle two
    else:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2.0

METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(median)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)