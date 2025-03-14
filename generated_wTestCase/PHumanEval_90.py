def next_smallest(lst):
    """
    Returns the 2nd smallest element of the list.
    Return None if there is no such element.
    """
    # Convert the list to a set to remove duplicates and sort it
    unique_sorted = sorted(set(lst))

    # Check if there are at least two unique elements
    if len(unique_sorted) < 2:
        return None

    # Return the second smallest element
    return unique_sorted[1]

def check(candidate):

    # Check some simple cases
    assert candidate([1, 2, 3, 4, 5]) == 2
    assert candidate([5, 1, 4, 3, 2]) == 2
    assert candidate([]) == None
    assert candidate([1, 1]) == None
    assert candidate([1,1,1,1,0]) == 1
    assert candidate([1, 0**0]) == None
    assert candidate([-35, 34, 12, -45]) == -35

    # Check some edge cases that are easy to work out by hand.
    assert True


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(next_smallest)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)