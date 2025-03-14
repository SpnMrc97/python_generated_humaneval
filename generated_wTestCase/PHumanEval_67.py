def fruit_distribution(s: str, n: int) -> int:
    """
    Calculate the number of mango fruits in the basket.

    Parameters:
    s (str): A string containing counts of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Extracting numbers from the string
    parts = s.split()
    apples = int(parts[0])
    oranges = int(parts[3])
    
    # Calculating the number of mangoes
    mangoes = n - apples - oranges
    return mangoes

def check(candidate):

    # Check some simple cases
    assert candidate("5 apples and 6 oranges",19) == 8
    assert candidate("5 apples and 6 oranges",21) == 10
    assert candidate("0 apples and 1 oranges",3) == 2
    assert candidate("1 apples and 0 oranges",3) == 2
    assert candidate("2 apples and 3 oranges",100) == 95
    assert candidate("2 apples and 3 oranges",5) == 0
    assert candidate("1 apples and 100 oranges",120) == 19


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(fruit_distribution)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)