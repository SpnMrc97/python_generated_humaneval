def encode(message):
    def shift_vowel(char):
        vowels = 'aeiouAEIOU'
        shifted_vowels = 'cgkqwCGKQW'
        if char in vowels:
            index = vowels.index(char)
            return shifted_vowels[index]
        return char

    encoded_message = []
    for char in message:
        # Swap the case of the letter
        swapped_char = char.swapcase()
        # Shift vowels if necessary
        encoded_char = shift_vowel(swapped_char)
        # Append to the result
        encoded_message.append(encoded_char)

    return ''.join(encoded_message)
