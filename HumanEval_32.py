import math

def poly(xs: list, x: float) -> float:
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def derivative(xs: list, x: float) -> float:
    return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0])


def find_zero(xs: list, initial_guess: float = 0.0, tolerance: float = 1e-7, max_iterations: int = 1000) -> float:
    x = initial_guess
    for _ in range(max_iterations):
        fx = poly(xs, x)
        if abs(fx) < tolerance:
            return x
        f_prime_x = derivative(xs, x)
        if f_prime_x == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x -= fx / f_prime_x
    raise ValueError("Maximum iterations exceeded. No solution found.")
