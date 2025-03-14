def fib4(n: int) -> int:
    """
    Computes the n-th element of the Fib4 number sequence.
    
    The Fib4 number sequence is defined as:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4
    
    Parameters:
    n (int): The index of the element to compute in the sequence.

    Returns:
    int: The n-th element of the Fib4 number sequence.
    """
    
    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Initialize the base values for fib4(0) to fib4(3)
    fib_values = [0, 0, 2, 0]
    
    # Compute fib4(n) iteratively
    for i in range(4, n + 1):
        next_value = fib_values[-1] + fib_values[-2] + fib_values[-3] + fib_values[-4]
        fib_values.append(next_value)
        fib_values.pop(0)  # Remove the oldest value to keep the list size constant
    
    return fib_values[-1]

METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(fib4)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)