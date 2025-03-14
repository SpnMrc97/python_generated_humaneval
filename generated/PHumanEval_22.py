from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """Filter a given list of any Python values to return only integers.
    
    Args:
        values (List[Any]): A list containing any type of Python values.
        
    Returns:
        List[int]: A list containing only the integer values from the input list.
        
    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]
