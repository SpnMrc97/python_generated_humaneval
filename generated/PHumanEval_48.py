def is_palindrome(text: str) -> bool:
    """
    Checks if the given string is a palindrome.
    
    Args:
        text (str): The string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
        
    Examples:
        >>> is_palindrome('')
        True
        >>> is_palindrome('aba')
        True
        >>> is_palindrome('aaaaa')
        True
        >>> is_palindrome('zbcd')
        False
    """
    # A palindrome reads the same forwards and backwards.
    # We can use slicing to reverse the string and compare with original.
    return text == text[::-1]
