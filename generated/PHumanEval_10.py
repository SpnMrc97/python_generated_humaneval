def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.

    The idea is to find the longest palindromic suffix and append the reverse of the prefix preceding it.
    
    Args:
        string (str): The input string.

    Returns:
        str: The shortest palindrome that starts with the input string.

    Examples:
        >>> make_palindrome('')
        ''
        >>> make_palindrome('cat')
        'catac'
        >>> make_palindrome('cata')
        'catac'
    """
    if is_palindrome(string):
        return string
    
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]
    
    return string + string[::-1]
