def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    if n == 1:
        # For a single-digit number, the only valid number is 1
        return 1

    # Total n-digit numbers: 9 * 10^(n-1)
    total_n_digit_numbers = 9 * (10 ** (n - 1))

    # Numbers starting with 1: 10^(n-1)
    start_with_1 = 10 ** (n - 1)

    # Numbers ending with 1: 9 * 10^(n-2)
    end_with_1 = 9 * (10 ** (n - 2))

    # Numbers starting and ending with 1: 10^(n-2)
    both_start_and_end_with_1 = 10 ** (n - 2)

    # Use the principle of inclusion-exclusion
    return start_with_1 + end_with_1 - both_start_and_end_with_1
