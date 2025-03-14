def is_simple_power(x, n):
    """Returns True if x is a simple power of n, otherwise False."""
    if x == 1:
        # Any number to the power of 0 is 1, hence 1 is a power of any number n (except n=0).
        return True
    if n < 2:
        # If n is less than 2, it cannot be a base for powers other than 1 when x=1.
        return False

    power = 1
    while power < x:
        power *= n
    return power == x
