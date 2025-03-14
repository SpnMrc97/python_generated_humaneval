from typing import List

def concatenate(strings: List[str]) -> str:
    """Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: A single string resulting from the concatenation of the input strings.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)
