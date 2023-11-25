from shingles import shingles

def test_shingles():
    # check for normal input
    assert shingles(['a', 'b', 'c', 'd'], 2) == {'a b', 'b c', 'c d'}
    #check for empty string
    assert shingles([], 2) == set()
    #check for k type string
    try:
        shingles(['a', 'b', 'c', 'd'], "k")
        assert False
    except TypeError:
        assert True
    #check for t type int
    try:
        shingles(2, 2)
        assert False
    except TypeError:
        assert True
    #check for k = 0 and expect ValueError("k is greater than the length of t")
    try:
        shingles(['a', 'b', 'c', 'd'], "4")
        assert False
    except TypeError:
        assert True
    #check for k = 0 and expect ValueError("k is less than 1")
    try:
        shingles(['a', 'b', 'c', 'd'], 0)
        assert False
    except ValueError:
        assert True
    #check when elements of t are not strings
    try:
        shingles(['a', 'b', 1, 'd'], 2)
        assert False
    except TypeError:
        assert True
