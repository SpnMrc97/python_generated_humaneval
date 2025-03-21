def is_simple_power(x, n):
    if x == 1:
        # 1 is a power of every integer n, as n**0 = 1 for any n
        return True
    if n <= 1:
        # If n is 1, only 1 can be a power of 1, otherwise return False
        return False
    
    current_power = n
    while current_power <= x:
        if current_power == x:
            return True
        current_power *= n
    
    return False
