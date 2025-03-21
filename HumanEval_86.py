def anti_shuffle(s):
    def sort_word(word):
        # Sort the characters in the word based on ASCII values.
        return ''.join(sorted(word))
    
    # Split the string into words using spaces as separators, keeping the spaces intact.
    words = s.split(' ')
    
    # Apply the sorting to each word and join them back together with spaces
    sorted_words = ' '.join(sort_word(word) for word in words)
    
    return sorted_words
