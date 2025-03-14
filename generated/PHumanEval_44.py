def change_base(x: int, base: int) -> str:
    """Change the numerical base of input number x to a given base.
    Return the string representation after the conversion.
    Only bases less than 10 are supported.
    
    Args:
        x (int): The number to convert.
        base (int): The base to convert to, must be less than 10.
        
    Returns:
        str: The base-converted number as a string.
        
    Raises:
        ValueError: If the base is not between 2 and 9.

    Examples:
        >>> change_base(8, 3)
        '22'
        >>> change_base(8, 2)
        '1000'
        >>> change_base(7, 2)
        '111'
    """
    if base < 2 or base >= 10:
        raise ValueError("Base must be between 2 and 9")

    if x == 0:
        return "0"

    result = []
    while x > 0:
        result.append(str(x % base))
        x //= base

    return ''.join(reversed(result))
