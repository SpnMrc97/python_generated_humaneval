def flip_case(string: str) -> str:
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string.
        
    Returns:
        str: The string with flipped case for each character.
    
    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return string.swapcase()
