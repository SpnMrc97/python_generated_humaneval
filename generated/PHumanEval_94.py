def is_prime(n):
    """Check if a number is a prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_digits(n):
    """Return the sum of the digits of a number."""
    return sum(int(digit) for digit in str(n))

def skjkasdkd(lst):
    """Find the largest prime in the list and return the sum of its digits."""
    largest_prime = -1
    for num in lst:
        if is_prime(num):
            largest_prime = max(largest_prime, num)
    
    if largest_prime == -1:
        return 0  # Return 0 if no prime number is found
    
    return sum_of_digits(largest_prime)
