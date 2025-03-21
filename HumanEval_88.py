def sort_array(array):
    # Check if the array is empty or has only one element
    if not array or len(array) == 1:
        return array.copy()
    
    # Calculate the sum of the first and last elements
    first_last_sum = array[0] + array[-1]

    # Determine the sorting order based on the sum
    if first_last_sum % 2 == 0:
        # Even sum, sort in descending order
        return sorted(array, reverse=True)
    else:
        # Odd sum, sort in ascending order
        return sorted(array)
