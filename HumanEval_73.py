def smallest_change(arr):
    # Initialize two pointers, one at the start and one at the end of the array
    left = 0
    right = len(arr) - 1
    
    # Initialize a counter for the number of changes required
    changes = 0
    
    # Loop until the two pointers meet in the middle
    while left < right:
        # If the elements at the two pointers are not equal, increment the change counter
        if arr[left] != arr[right]:
            changes += 1
        # Move the pointers towards the center
        left += 1
        right -= 1
    
    return changes
