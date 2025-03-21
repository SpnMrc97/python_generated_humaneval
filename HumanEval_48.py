def is_palindrome(text: str) -> bool:
    # Compare the string with its reverse
    return text == text[::-1]
