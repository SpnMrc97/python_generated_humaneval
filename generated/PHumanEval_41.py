def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between two sets of n cars moving towards each other.
    
    :param n: The number of cars in each set.
    :return: The total number of collisions.
    """
    # Each car from the left set collides with each car from the right set.
    # Therefore, the number of collisions is simply the product of the two sets.
    return n * n
