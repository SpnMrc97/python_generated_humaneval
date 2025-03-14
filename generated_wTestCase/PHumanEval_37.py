def sort_even(l: list) -> list:
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal
    to the values of the even indices of l, but sorted.
    """
    # Extract even-indexed elements
    even_indexed_elements = [l[i] for i in range(len(l)) if i % 2 == 0]
    
    # Sort the even-indexed elements
    even_indexed_elements_sorted = sorted(even_indexed_elements)
    
    # Construct the new list with sorted even indices
    result = l[:]  # Make a copy of the original list
    even_index = 0
    
    for i in range(len(result)):
        if i % 2 == 0:
            result[i] = even_indexed_elements_sorted[even_index]
            even_index += 1
    
    return result

METADATA = {}


def check(candidate):
    assert tuple(candidate([1, 2, 3])) == tuple([1, 2, 3])
    assert tuple(candidate([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == tuple([-10, 3, -5, 2, -3, 3, 5, 0, 9, 1, 123])
    assert tuple(candidate([5, 8, -12, 4, 23, 2, 3, 11, 12, -10])) == tuple([-12, 8, 3, 4, 5, 2, 12, 11, 23, -10])


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(sort_even)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)