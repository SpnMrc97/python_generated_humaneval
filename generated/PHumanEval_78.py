def hex_key(num):
    """Counts the number of prime hexadecimal digits in a given hexadecimal number string."""
    # Define the set of prime hexadecimal digits
    prime_hex_digits = {'2', '3', '5', '7', 'B', 'D'}
    
    # Initialize a counter for prime digits
    prime_count = 0

    # Iterate over each character in the input string
    for char in num:
        # Increment the counter if the character is in the set of prime digits
        if char in prime_hex_digits:
            prime_count += 1
    
    return prime_count
