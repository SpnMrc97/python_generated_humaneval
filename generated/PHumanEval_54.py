def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    
    :param s0: First string to compare
    :param s1: Second string to compare
    :return: True if both strings contain the same characters, False otherwise
    """
    # Convert both strings to sets of characters and compare
    return set(s0) == set(s1)
