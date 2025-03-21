def fruit_distribution(s, n):
    
    # Split the string to extract numbers
    parts = s.split()
    
    # Convert the parts that represent numbers into integers
    apples = int(parts[0])
    oranges = int(parts[3])
    
    # Calculate the number of mangoes
    mangoes = n - apples - oranges
    
    return mangoes
