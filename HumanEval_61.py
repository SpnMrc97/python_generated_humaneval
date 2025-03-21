def correct_bracketing(brackets: str) -> bool:
    balance = 0
    for char in brackets:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        # If balance goes negative, there's a closing bracket without a matching opening bracket
        if balance < 0:
            return False
    # In the end, balance should be zero if all opening brackets have matching closing brackets
    return balance == 0
