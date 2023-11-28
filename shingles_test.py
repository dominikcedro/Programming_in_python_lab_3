"""
@author Dominik Cedro
"""
from shingles import shingles


def test_shingles_typical():
    # check for normal input
    assert shingles(['a', 'b', 'c', 'd'], 2) == {'a b': 1, 'b c': 1, 'c d': 1}
    # check for empty string
    assert shingles([], 2) == set()
    # check for k - type string
    try:
        shingles(['a', 'b', 'c', 'd'], "k")
        assert False
    except TypeError:
        assert True
    # check for t - type int
    try:
        shingles(2, 2)
        assert False
    except TypeError:
        assert True
    # check when elements of t are not strings
    try:
        shingles(['a', 'b', 1, 'd'], 2)
        assert False
    except TypeError:
        assert True


def test_shingles_border():
    # check for k = 1
    assert shingles(['a', 'b', 'c', 'd'], 1) == {'a': 1, 'b': 1, 'c': 1, 'd': 1}
    # check for k = 0 and expect ValueError("k is less than 1")
    try:
        shingles(['a', 'b', 'c', 'd'], 0)
        assert False
    except ValueError:
        assert True
    # check for k = len(t)
    assert shingles(['a', 'b', 'c', 'd'], 4) == {'a b c d': 1}
    # check for k = len(t) - 1
    assert shingles(['a', 'b', 'c', 'd'], 3) == {'a b c': 1, 'b c d': 1}
    # check for k = 0
    try:
        shingles(['a', 'b', 'c', 'd'], 0)
        assert False
    except ValueError:
        assert True
    # check for k = -1
    try:
        shingles(['a', 'b', 'c', 'd'], -1)
        assert False
    except ValueError:
        assert True
