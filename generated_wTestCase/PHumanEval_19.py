from typing import List

def sort_numbers(numbers: str) -> str:
    """ 
    Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    
    >>> sort_numbers('three one five')
    'one three five'
    """
    numeral_to_int = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    
    int_to_numeral = {v: k for k, v in numeral_to_int.items()}
    
    # Split the input string into a list of numerals
    numeral_list = numbers.split()
    
    # Convert numerals to integers for sorting
    int_list = [numeral_to_int[numeral] for numeral in numeral_list]
    
    # Sort the integers
    sorted_int_list = sorted(int_list)
    
    # Convert sorted integers back to numerals
    sorted_numeral_list = [int_to_numeral[num] for num in sorted_int_list]
    
    # Join the sorted numerals into a space-delimited string
    return ' '.join(sorted_numeral_list)

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == ''
    assert candidate('three') == 'three'
    assert candidate('three five nine') == 'three five nine'
    assert candidate('five zero four seven nine eight') == 'zero four five seven eight nine'
    assert candidate('six five four three two one zero') == 'zero one two three four five six'


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(sort_numbers)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)