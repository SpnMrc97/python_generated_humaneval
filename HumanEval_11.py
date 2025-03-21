from typing import List

def string_xor(a: str, b: str) -> str:
    # Ensure both strings are of equal length
    if len(a) != len(b):
        raise ValueError("Input strings must be of the same length.")
    
    # Perform XOR operation for each pair of corresponding characters
    result = []
    for char_a, char_b in zip(a, b):
        # XOR operation and convert back to string
        xor_result = str(int(char_a) ^ int(char_b))
        result.append(xor_result)
    
    # Join the list of results into a single string
    return ''.join(result)
