def change_base(x: int, base: int) -> str:
    if x < 0:
        raise ValueError("The input number must be non-negative.")
    if not (2 <= base < 10):
        raise ValueError("Base must be between 2 and 9.")

    if x == 0:
        return "0"

    digits = []
    while x > 0:
        remainder = x % base
        digits.append(str(remainder))
        x = x // base

    # Since the remainders are collected in reverse order, reverse the list
    digits.reverse()

    return ''.join(digits)
