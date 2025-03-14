def fruit_distribution(s: str, n: int) -> int:
    """
    Calculate the number of mango fruits in the basket.

    Parameters:
    s (str): A string containing counts of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Extracting numbers from the string
    parts = s.split()
    apples = int(parts[0])
    oranges = int(parts[3])
    
    # Calculating the number of mangoes
    mangoes = n - apples - oranges
    return mangoes
