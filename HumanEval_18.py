def how_many_times(string: str, substring: str) -> int:
    count = 0
    start = 0

    while start <= len(string) - len(substring):
        # Find the next occurrence of the substring
        pos = string.find(substring, start)
        if pos != -1:
            count += 1
            # Move start to the next position after the current match for overlap
            start = pos + 1
        else:
            break

    return count
