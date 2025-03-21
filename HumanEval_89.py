def encrypt(s):
    def shift_char(c):
        if 'a' <= c <= 'z':
            # Calculate new character position with rotation by 4
            new_pos = (ord(c) - ord('a') + 4) % 26
            return chr(ord('a') + new_pos)
        else:
            # If the character is not a lowercase letter, leave it unchanged
            return c

    return ''.join(shift_char(c) for c in s)
