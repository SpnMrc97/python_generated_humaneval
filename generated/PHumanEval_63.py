def fibfib(n: int) -> int:
    """Compute the n-th element of the FibFib number sequence."""
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    
    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize the first three elements of the sequence
    fibfib_seq = [0, 0, 1]
    
    # Compute the sequence up to the n-th element
    for i in range(3, n + 1):
        next_value = fibfib_seq[i - 1] + fibfib_seq[i - 2] + fibfib_seq[i - 3]
        fibfib_seq.append(next_value)
    
    return fibfib_seq[n]
