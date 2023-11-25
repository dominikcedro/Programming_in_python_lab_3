"""
@author Dominik Cedro
"""

def shingles(t, k):
    """    This function takes a list of strings and returns a set of k-shingles.

    Args:
        t: list of strings
        k: integer

    Returns:
        shingles_set: set of k-shingles

    Raises:
        TypeError: if t is not a list
        TypeError: if k is not an integer
        ValueError: if k is greater than the length of t
        ValueError: if k is less than 1

    """
    if not isinstance(t, list):
        raise TypeError("t is not a list")
    for i in t:
        if not isinstance(i, str):
            raise TypeError("elements of t are not strings")
    if not isinstance(k, int):
        raise TypeError("k is not a integer")
    if t == []:
        return set()
    if k > len(t):
        raise ValueError("k is greater than the length of t")
    if k < 1:
        raise ValueError("k is less than 1")
    #create and empty set
    shingles_set = set()
    for i in range(len(t) - k + 1):
        shingle = ' '.join(t[i:i+k])
        # add the shingle to the set
        shingles_set.add(shingle)
    return shingles_set

