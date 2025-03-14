from collections import Counter

def search(lst):
    # Count the frequency of each element in the list
    freq = Counter(lst)
    
    # Initialize a variable to store the greatest integer meeting the condition
    greatest_valid_integer = -1
    
    # Iterate over the unique elements in the list
    for num in freq:
        # Check if the frequency is greater than or equal to the integer value itself
        if freq[num] >= num:
            # Update the greatest_valid_integer if the current number is greater
            greatest_valid_integer = max(greatest_valid_integer, num)
    
    return greatest_valid_integer
