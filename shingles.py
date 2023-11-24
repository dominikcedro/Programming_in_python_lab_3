"""
@author Dominik Cedro
"""

from typing import List

def shingles(t: List[str], k: int) -> List[str]:
    if not isinstance(t, list):
        raise TypeError("t is not a list")
    if not isinstance(k, int):
        raise TypeError("k is not a str")
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




