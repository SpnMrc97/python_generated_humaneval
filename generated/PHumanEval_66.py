def digitSum(s: str) -> int:
    """
    Calculate the sum of ASCII values of uppercase characters in the input string.

    Parameters:
    s (str): The input string.

    Returns:
    int: Sum of ASCII values of uppercase characters in the string.
    """
    return sum(ord(char) for char in s if char.isupper())
