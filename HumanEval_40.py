def triples_sum_to_zero(l: list) -> bool:
    # Sort the list to easily use the two-pointer approach
    l.sort()

    # Iterate over the list, considering each element as a potential first element of the triplet
    for i in range(len(l) - 2):
        # To avoid duplicates, skip the same element
        if i > 0 and l[i] == l[i - 1]:
            continue
        
        # Use two pointers to find the other two numbers
        left, right = i + 1, len(l) - 1
        while left < right:
            total = l[i] + l[left] + l[right]
            if total == 0:
                return True
            elif total < 0:
                left += 1
            else:
                right -= 1

    return False
