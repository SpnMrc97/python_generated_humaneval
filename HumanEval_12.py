from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    
    # Initialize the longest string as the first one in the list
    longest_string = strings[0]
    
    # Iterate over the list and find the longest string
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    
    return longest_string
