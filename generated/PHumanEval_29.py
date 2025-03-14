from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The list of strings to filter.
        prefix (str): The prefix to filter strings by.

    Returns:
        List[str]: A list of strings that start with the given prefix.

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]
