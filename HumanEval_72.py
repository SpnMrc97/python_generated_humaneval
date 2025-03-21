def will_it_fly(q, w):
    # Check if the list q is a palindrome
    is_balanced = q == q[::-1]
    
    # Calculate the sum of elements in q
    total_weight = sum(q)
    
    # Check if the object is balanced and the total weight is within the limit
    return is_balanced and total_weight <= w
