def encode(message):
    """
    Encodes the given message by swapping the case of all letters
    and replacing all vowels with the letter that appears 2 places
    ahead of that vowel in the English alphabet.

    Parameters:
    message (str): The input string containing only letters.

    Returns:
    str: The encoded message.
    """
    # Define a mapping for vowels to their replacements
    vowel_mapping = {
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
        'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'
    }
    
    encoded_message = []

    for char in message:
        if char in vowel_mapping:
            # Replace vowel with its corresponding mapped character
            encoded_message.append(vowel_mapping[char])
        else:
            # Swap case of the character
            encoded_message.append(char.swapcase())

    return ''.join(encoded_message)
