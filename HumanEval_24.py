def largest_divisor(n: int) -> int:
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return 1  # If no divisor is found, return 1 (since 1 divides any number)
