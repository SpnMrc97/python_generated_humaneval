def encode_shift(s: str) -> str:
    """
    Returns the encoded string by shifting every character by 5 positions in the alphabet.
    """
    return "".join(
        [chr(((ord(ch) + 5 - ord('a')) % 26) + ord('a')) for ch in s]
    )


def decode_shift(s: str) -> str:
    """
    Takes as input a string encoded with the encode_shift function.
    Returns the decoded string by reversing the shift.
    """
    return "".join(
        [chr(((ord(ch) - 5 - ord('a')) % 26) + ord('a')) for ch in s]
    )
