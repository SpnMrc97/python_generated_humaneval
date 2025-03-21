from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    # Check for the number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check for odd numbers from 3 to sqrt(n)
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 2
    
    # If n is still greater than 2, then it must be a prime number
    if n > 2:
        factors.append(n)
    
    return factors
