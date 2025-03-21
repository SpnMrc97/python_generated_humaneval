def fibfib(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    
    # Initialize base cases
    fibfib_sequence = [0, 0, 1]
    
    # If n is less than 3, return the corresponding base case
    if n < 3:
        return fibfib_sequence[n]
    
    # Fill the sequence up to the n-th element
    for i in range(3, n + 1):
        next_value = fibfib_sequence[i - 1] + fibfib_sequence[i - 2] + fibfib_sequence[i - 3]
        fibfib_sequence.append(next_value)
    
    return fibfib_sequence[n]
