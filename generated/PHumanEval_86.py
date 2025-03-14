def anti_shuffle(s):
    """
    Takes a string and returns an ordered version of it where each word's
    characters are sorted in ascending ASCII order. The order of words and
    spaces in the sentence is preserved.
    
    Args:
    s (str): The input string.
    
    Returns:
    str: The string with each word's characters sorted.
    """
    def sort_word(word):
        return ''.join(sorted(word))
    
    result = []
    current_word = []

    for char in s:
        if char.isalpha():
            current_word.append(char)
        else:
            if current_word:
                result.append(sort_word(current_word))
                current_word = []
            result.append(char)
    
    if current_word:
        result.append(sort_word(current_word))
    
    return ''.join(result)
