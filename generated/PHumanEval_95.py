def check_dict_case(input_dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False if the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345"}) should return True.
    """
    if not input_dict:
        return False

    keys = input_dict.keys()
    
    all_lower = all(isinstance(key, str) and key.islower() for key in keys)
    all_upper = all(isinstance(key, str) and key.isupper() for key in keys)
    
    return all_lower or all_upper
