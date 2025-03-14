def correct_bracketing(brackets: str) -> bool:
    """
    Checks if every opening bracket '(' in the string has a corresponding closing bracket ')'.

    Args:
    brackets (str): A string consisting of '(' and ')'.

    Returns:
    bool: True if the brackets are correctly balanced, False otherwise.

    Examples:
    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    balance = 0
    for char in brackets:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        
        # If balance goes negative, there are unmatched closing brackets
        if balance < 0:
            return False
    
    # If balance is zero, all brackets are matched
    return balance == 0
