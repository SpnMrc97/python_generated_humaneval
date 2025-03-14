def numerical_letter_grade(grades):
    """
    Convert a list of GPAs to their corresponding letter grades based on the given grading scale.

    Args:
    grades (list of float): A list containing GPA values.

    Returns:
    list of str: A list containing the corresponding letter grades.
    """
    
    # Define the mapping of GPA ranges to letter grades
    grade_mapping = [
        (4.0, 'A+'),
        (3.7, 'A'),
        (3.3, 'A-'),
        (3.0, 'B+'),
        (2.7, 'B'),
        (2.3, 'B-'),
        (2.0, 'C+'),
        (1.7, 'C'),
        (1.3, 'C-'),
        (1.0, 'D+'),
        (0.7, 'D'),
        (0.0, 'D-')
    ]
    
    # Initialize the list to store the letter grades
    letter_grades = []

    # Iterate over each GPA in the input list
    for gpa in grades:
        # Find the corresponding letter grade for each GPA
        for threshold, letter in grade_mapping:
            if gpa >= threshold:
                letter_grades.append(letter)
                break

    return letter_grades
