import math
from scipy.optimize import brentq

def poly(xs: list, x: float) -> float:
    """
    Evaluates a polynomial with coefficients `xs` at point `x`.
    The polynomial is given by:
    xs[0] + xs[1] * x + xs[2] * x^2 + ... + xs[n] * x^n
    """
    return sum(coeff * (x ** i) for i, coeff in enumerate(xs))

def find_zero(xs: list) -> float:
    """
    Finds a root of the polynomial with coefficients `xs`.
    The function returns a single zero point, even if there are multiple.
    It expects `xs` to have an even number of coefficients with the largest
    non-zero leading term as it guarantees a solution.

    Args:
        xs (list): Coefficients of the polynomial.

    Returns:
        float: A zero of the polynomial.

    Raises:
        ValueError: If no zero is found within the interval [-1000, 1000].

    Examples:
        >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
        -0.5

        >>> round(find_zero([-6, 11, -6, 1]), 2) # f(x) = -6 + 11x - 6x^2 + x^3
        1.0
    """
    # Define the polynomial function for root finding
    def polynomial(x):
        return poly(xs, x)
    
    # Use a root-finding algorithm to find a zero of the polynomial
    try:
        # Try to find a root within a reasonable interval
        root = brentq(polynomial, -1000, 1000)
    except ValueError as e:
        # If no root is found, raise an error
        raise ValueError("No zero found within the interval [-1000, 1000].") from e
    
    return root

METADATA = {}


def check(candidate):
    import math
    import random
    rng = random.Random(42)
    import copy
    for _ in range(100):
        ncoeff = 2 * rng.randint(1, 4)
        coeffs = []
        for _ in range(ncoeff):
            coeff = rng.randint(-10, 10)
            if coeff == 0:
                coeff = 1
            coeffs.append(coeff)
        solution = candidate(copy.deepcopy(coeffs))
        assert math.fabs(poly(coeffs, solution)) < 1e-4


import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check(find_zero)  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)