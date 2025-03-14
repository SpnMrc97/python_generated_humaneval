def encrypt(s):
    """Encrypts the input string by rotating each alphabet character
    down by four places.
    
    Args:
        s (str): The input string to be encrypted.
        
    Returns:
        str: The encrypted string with each character rotated.
    """
    result = []
    for char in s:
        if 'a' <= char <= 'z':
            new_char = chr(((ord(char) - ord('a') + 4) % 26) + ord('a'))
            result.append(new_char)
        else:
            # If the character is not a lowercase letter, it remains unchanged
            result.append(char)
    return ''.join(result)
