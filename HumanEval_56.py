def correct_bracketing(brackets: str) -> bool:
    count = 0

    for bracket in brackets:
        if bracket == "<":
            count += 1
        elif bracket == ">":
            count -= 1
        
        # If count goes negative, it means there is a mismatch
        if count < 0:
            return False
    
    # If count is not zero, there are unmatched opening brackets
    return count == 0
