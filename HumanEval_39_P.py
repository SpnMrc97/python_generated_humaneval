from math import isqrt

def is_prime(num: int) -> bool:
    """Return True if the number is prime, else False."""
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

def prime_fib(n: int) -> int:
    """
    Return the n-th number that is both a Fibonacci number and prime.
    """
    fib1, fib2 = 1, 1
    count = 0
    
    while True:
        if is_prime(fib1):
            count += 1
            if count == n:
                return fib1