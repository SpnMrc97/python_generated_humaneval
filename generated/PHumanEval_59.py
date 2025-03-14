def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    
    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    
    largest_factor = 1

    # Remove the factors of 2
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    # Remove the odd factors from 3 upwards
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_factor = factor
            n //= factor
        factor += 2

    # If n is a prime number greater than 2 at this point, then it is the largest prime factor
    if n > 2:
        largest_factor = n

    return largest_factor
