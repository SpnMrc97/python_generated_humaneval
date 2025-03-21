def solve(N):
    # Convert the integer to a string to iterate over each character
    digit_sum = sum(int(digit) for digit in str(N))
    
    # Convert the sum of digits to a binary string and remove the '0b' prefix
    binary_result = bin(digit_sum)[2:]
    
    return binary_result
