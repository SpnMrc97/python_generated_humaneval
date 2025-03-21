def get_row(lst, x):
    result = []
    
    # Iterate over the list with row indices
    for row_index, row in enumerate(lst):
        # Iterate over each element in the row with column indices
        for col_index, value in enumerate(row):
            # Check if the element is equal to x
            if value == x:
                # Append the coordinate as a tuple to the result
                result.append((row_index, col_index))
    
    # Sort the result first by row_index, then by col_index descending within each row
    result.sort(key=lambda coord: (coord[0], -coord[1]))
    
    return result
