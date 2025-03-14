from typing import List

def below_zero(operations: List[int]) -> bool:
    """Detects if at any point the balance of a bank account falls below zero.

    Args:
        operations (List[int]): A list of integers representing deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero at any point, otherwise False.

    Examples:
        >>> below_zero([1, 2, 3])
        False
        >>> below_zero([1, 2, -4, 5])
        True
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False
