import pytest
from shingle import parser, get_input, most_common, shingle_execute
import sys



def test_parser_typical():
    #normal inputs
    sys.argv = ['test_shingle.py', '-n', '1', '-k', '1']
    assert parser() == (1, 1)
    #normal inputs
    sys.argv = ['test_shingle.py', '-n', '2', '-k', '2']
    assert parser() == (2, 2)

def test_parser_border():
    # no argument k
    sys.argv = ['test_shingle.py', '-n', '1']
    with pytest.raises(SystemExit):
        parser()
    # no argument n
    sys.argv = ['test_shingle.py', '-k', '1']
    with pytest.raises(SystemExit):
        parser()
    # argument type float
    sys.argv = ['test_shingle.py', '-n', '1.0', '-k', '1']
    with pytest.raises(SystemExit):
        parser()
    #argument type list
    sys.argv = ['test_shingle.py', '-n', '[1]', '-k', '1']
    with pytest.raises(SystemExit):
        parser()

