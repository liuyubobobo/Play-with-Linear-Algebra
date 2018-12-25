EPSILON = 1e-8


def is_zero(x):
    return abs(x) < EPSILON


def is_equal(a, b):
    return abs(a - b) < EPSILON