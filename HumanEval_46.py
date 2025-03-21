def fib4(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Base cases
    if n == 0 or n == 1 or n == 3:
        return 0
    elif n == 2:
        return 2

    # Initialize the first four elements of the sequence
    a, b, c, d = 0, 0, 2, 0

    # Iteratively compute the next elements up to n
    for _ in range(4, n + 1):
        next_val = a + b + c + d
        a, b, c, d = b, c, d, next_val

    return d
