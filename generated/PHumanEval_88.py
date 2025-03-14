def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting.
    Sort the array in ascending order if the sum of the first and last index values is odd,
    or sort it in descending order if the sum is even.

    Note:
    * Do not change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    if not array:
        return []

    first_value = array[0]
    last_value = array[-1]
    sum_first_last = first_value + last_value

    if sum_first_last % 2 == 0:
        # Sort in descending order
        return sorted(array, reverse=True)
    else:
        # Sort in ascending order
        return sorted(array)
