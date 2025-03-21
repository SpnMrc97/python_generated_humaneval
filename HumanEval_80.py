def is_happy(s):
    # Check if the string length is less than 3
    if len(s) < 3:
        return False
    
    # Iterate through the string and check every 3 consecutive letters
    for i in range(len(s) - 2):
        # Extract the current group of 3 consecutive letters
        triplet = s[i:i+3]
        # If the length of the set of the triplet (unique letters) is not 3, return False
        if len(set(triplet)) != 3:
            return False
    
    # If all consecutive triplets are distinct, return True
    return True
