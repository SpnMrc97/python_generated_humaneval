from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    :param paren_string: A string with groups of nested parentheses separated by spaces.
    :return: A list of integers representing the deepest level of nesting for each group.
    
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def max_nesting_level(paren_group: str) -> int:
        max_depth = 0
        current_depth = 0
        
        for char in paren_group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
                if current_depth < 0:
                    raise ValueError("Unmatched closing parenthesis encountered.")
        
        if current_depth != 0:
            raise ValueError("Unmatched opening parenthesis encountered.")
        
        return max_depth
    
    groups = paren_string.split()
    return [max_nesting_level(group) for group in groups]
