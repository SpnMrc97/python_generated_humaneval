def encode_cyclic(s: str) -> str:
    """
    Returns an encoded string by cycling groups of three characters.
    """
    # Split string into groups, each of length 3
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    # Cycle elements in each group, unless the group has fewer elements than 3
    encoded_groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(encoded_groups)

def decode_cyclic(s: str) -> str:
    """
    Takes as input a string encoded with the encode_cyclic function and returns the decoded string.
    """
    # Split string into groups, each of length 3
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    # Reverse cycle elements in each group, unless the group has fewer elements than 3
    decoded_groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(decoded_groups)
