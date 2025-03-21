def iscube(a):
    # Calculate the cube root of the absolute value of a
    cube_root = round(abs(a) ** (1/3))

    # Check if the cube of the calculated root equals the original number
    return cube_root ** 3 == abs(a)
