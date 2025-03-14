def get_row(lst, x):
    """
    You are given a 2-dimensional data, as nested lists,
    which is similar to a matrix. However, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return a list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, column), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
    coordinates = []
    
    for row_index, row in enumerate(lst):
        for col_index, value in enumerate(row):
            if value == x:
                coordinates.append((row_index, col_index))
    
    # Sort the coordinates: first by row in ascending order, 
    # then by column in descending order for the same row.
    coordinates.sort(key=lambda coord: (coord[0], -coord[1]))
    
    return coordinates
