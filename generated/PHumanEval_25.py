from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed the number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors.
    
    Args:
    n (int): The integer to factorize.
    
    Returns:
    List[int]: A list of prime factors.
    
    Examples:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    if n <= 1:
        return []
    
    factors = []
    # Check for number of 2s as factors
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check for odd factors from 3 to sqrt(n)
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 2
    
    # If n becomes a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors
