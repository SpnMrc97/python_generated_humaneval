def count_distinct_characters(string: str) -> int:
    # Convert the string to lowercase to ignore case differences
    lowercase_string = string.lower()
    
    # Use a set to find distinct characters
    distinct_characters = set(lowercase_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)
