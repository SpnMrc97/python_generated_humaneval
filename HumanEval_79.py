def decimal_to_binary(decimal):
    # Convert the decimal number to a binary string, omitting the '0b' prefix
    binary_str = bin(decimal)[2:]
    
    # Format and return the binary string with 'db' at both ends
    return f"db{binary_str}db"
