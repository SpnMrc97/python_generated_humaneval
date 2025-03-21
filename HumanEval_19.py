from typing import List

def sort_numbers(numbers: str) -> str:
    # Mapping from word to number
    word_to_number = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    
    # Mapping from number to word
    number_to_word = {v: k for k, v in word_to_number.items()}
    
    # Split the input string into words
    words = numbers.split()
    
    # Convert words to numbers
    number_list = [word_to_number[word] for word in words]
    
    # Sort the numbers
    number_list.sort()
    
    # Convert numbers back to words
    sorted_words = [number_to_word[number] for number in number_list]
    
    # Join the words back into a string
    return ' '.join(sorted_words)
