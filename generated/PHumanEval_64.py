def vowels_count(s: str) -> int:
    """Returns the number of vowels in the given string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel
    only when it is at the end of the string.
    
    Args:
        s (str): The input string.
        
    Returns:
        int: The number of vowels in the string.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    s = s.lower()  # Convert the string to lowercase to handle case insensitivity
    count = sum(1 for char in s if char in vowels)
    
    # Check if 'y' is at the end and add to count if it's there
    if s.endswith('y'):
        count += 1
    
    return count
