def check_dict_case(d):
    if not d:
        return False

    # Check if all keys are strings
    if not all(isinstance(key, str) for key in d):
        return False

    # Check if all keys are lowercase
    all_lower = all(key.islower() for key in d)
    
    # Check if all keys are uppercase
    all_upper = all(key.isupper() for key in d)
    
    # Return True if all keys are either all lowercase or all uppercase
    return all_lower or all_upper
