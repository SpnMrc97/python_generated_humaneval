def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    this function plucks one of the nodes and returns it.
    The plucked node is the node with the smallest even value.
    If multiple nodes with the same smallest even value are found, return the node that has the smallest index.

    The plucked node should be returned in a list, [smallest_value, its_index].
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]

    Example 3:
        Input: []
        Output: []

    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
    """
    if not arr:
        return []

    smallest_even = float('inf')
    smallest_index = -1

    for index, value in enumerate(arr):
        if value % 2 == 0:
            if value < smallest_even:
                smallest_even = value
                smallest_index = index

    return [smallest_even, smallest_index] if smallest_index != -1 else []
