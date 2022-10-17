def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    if x < 0:
        print("Must be a Positive Integer")
        return None
    if x == 1:
        print("Finished!")
        return x

    if x % 2 == 0:
        x = x//2
        print(x)
        return hailstone(x)
    x = x * 3 + 1
    print(x)
    return hailstone(x)


hailstone(10)
