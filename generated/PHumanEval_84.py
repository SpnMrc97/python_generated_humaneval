def solve(N):
    """
    Given a positive integer N, return the total sum of its digits in binary.

    Parameters:
        N (int): A non-negative integer (0 ≤ N ≤ 10000).

    Returns:
        str: The binary representation of the sum of the digits of N.
    """
    # Calculate the sum of the digits of N
    digit_sum = sum(int(digit) for digit in str(N))
    
    # Convert the sum to binary and return the binary string (excluding the '0b' prefix)
    return bin(digit_sum)[2:]
