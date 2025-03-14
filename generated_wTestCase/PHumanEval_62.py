def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial represented by its coefficients.
    
    :param xs: List of coefficients where xs[i] corresponds to the coefficient of x^i.
    :return: List of coefficients of the derivative polynomial.
    
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Calculate the derivative by multiplying each coefficient by its power index
    derivative_coeffs = [i * xs[i] for i in range(1, len(xs))]
    return derivative_coeffs

METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert candidate([1, 2, 3]) == [2, 6]
    assert candidate([3, 2, 1]) == [2, 2]
    assert candidate([3, 2, 1, 0, 4]) == [2, 2, 0, 16]
    assert candidate([1]) == []


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(derivative)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)