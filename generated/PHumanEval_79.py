def decimal_to_binary(decimal):
    """
    Converts a decimal number to its binary representation and wraps the binary
    string with 'db' at the beginning and end.

    Args:
        decimal (int): The decimal number to convert.

    Returns:
        str: The binary representation of the decimal number with 'db' at the
             start and end.
    """
    # Convert the decimal number to binary and remove the '0b' prefix
    binary_representation = bin(decimal)[2:]
    
    # Format with 'db' at the beginning and end
    result = f"db{binary_representation}db"
    
    return result
