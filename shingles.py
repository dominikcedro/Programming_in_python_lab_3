"""
@author Dominik Cedro
"""

def shingles(t,k):
    """Returns a set of k-shingles of a given text t.

    Args:
        t (str): text
        k (int): shingle length
    Returns:
        set: set of k-shingles

    """

    return set([t[i:i+k] for i in range(len(t)-k+1)])



