def total_match(lst1, lst2):
    """
    Accepts two lists of strings and returns the list that has the total number of characters
    in all strings of the list less than the other list. If the two lists have the same number
    of characters, returns the first list.

    Args:
    lst1 (list of str): The first list of strings.
    lst2 (list of str): The second list of strings.

    Returns:
    list of str: The list with fewer total characters, or the first list if they are equal.
    """
    
    # Calculate the total number of characters in each list
    total_chars_lst1 = sum(len(s) for s in lst1)
    total_chars_lst2 = sum(len(s) for s in lst2)

    # Compare the total characters and return the appropriate list
    if total_chars_lst1 < total_chars_lst2:
        return lst1
    else:
        return lst2

def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([], []) == []
    assert candidate(['hi', 'admin'], ['hi', 'hi']) == ['hi', 'hi']
    assert candidate(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    assert candidate(['4'], ['1', '2', '3', '4', '5']) == ['4']
    assert candidate(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
    assert candidate(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']


    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([], ['this']) == []
    assert candidate(['this'], []) == []


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(total_match)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)