def is_bored(S):
    """
    Count the number of sentences that start with the word 'I'.
    Sentences are delimited by '.', '?' or '!'.
    
    Parameters:
    S (str): A string containing multiple sentences.
    
    Returns:
    int: The count of sentences starting with 'I'.
    
    Examples:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    # Split the string into sentences based on delimiters: '.', '?', '!'
    sentences = [sentence.strip() for sentence in re.split(r'[.!?]', S)]
    
    # Count how many sentences start with the word 'I'
    boredom_count = sum(1 for sentence in sentences if sentence.startswith('I'))
    
    return boredom_count