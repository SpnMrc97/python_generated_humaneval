def triples_sum_to_zero(l: list) -> bool:
    """
    triples_sum_to_zero takes a list of integers as an input.
    It returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    n = len(l)
    if n < 3:
        return False

    # Sort the list to use two-pointer technique
    l.sort()

    for i in range(n - 2):
        # Avoid duplicates for the first number
        if i > 0 and l[i] == l[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            current_sum = l[i] + l[left] + l[right]

            if current_sum == 0:
                return True
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return False
