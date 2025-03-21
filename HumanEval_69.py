from collections import Counter

def search(lst):
    # Use Counter to count the frequencies of each element in the list
    frequency = Counter(lst)
    
    # Find all values where the integer is less than or equal to its frequency
    valid_numbers = [num for num, count in frequency.items() if num <= count]
    
    # Return the greatest integer from the valid numbers or -1 if there are none
    return max(valid_numbers) if valid_numbers else -1
