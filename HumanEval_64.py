def vowels_count(s):
    s = s.lower()
    count = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for i, char in enumerate(s):
        if char in vowels:
            count += 1
        elif char == 'y' and i == len(s) - 1:
            count += 1
    return count
