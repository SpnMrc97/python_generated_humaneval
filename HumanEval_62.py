def derivative(xs: list):
    # Skip the first element because its derivative is zero (constant term)
    return [xs[i] * i for i in range(1, len(xs))]
