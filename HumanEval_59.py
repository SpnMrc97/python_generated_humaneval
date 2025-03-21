def largest_prime_factor(n: int) -> int:
    largest_factor = None
    # Divide n by 2 until it becomes odd
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    # Check for odd factors from 3 onwards
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_factor = factor
            n //= factor
        factor += 2

    # If n becomes a prime number greater than 2
    if n > 2:
        largest_factor = n

    return largest_factor
