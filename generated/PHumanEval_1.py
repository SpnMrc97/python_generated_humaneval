from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ 
    Input to this function is a string containing multiple groups of nested parentheses. 
    Your goal is to separate those groups into separate strings and return the list of those. 
    Separate groups are balanced (each open brace is properly closed) and not nested within each other.
    Ignore any spaces in the input string.
    
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    result = []
    current_group = []
    balance = 0
    
    # Iterate over each character in the string
    for char in paren_string:
        current_group.append(char)
        
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        
        # When balance is zero, it means we have a balanced group
        if balance == 0 and current_group:
            result.append(''.join(current_group))
            current_group = []
    
    return result
