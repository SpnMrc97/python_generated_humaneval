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
