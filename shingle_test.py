import pytest
from _pytest import monkeypatch

from shingle import parser, get_input, most_common, shingle_execute
import sys
from io import StringIO
from unittest import mock


def test_parser_typical():
    #normal inputs
    sys.argv = ['test_shingle.py', '-n', '1', '-k', '1']
    assert parser() == (1, 1)
    #normal inputs
    sys.argv = ['test_shingle.py', '-n', '2', '-k', '2']
    assert parser() == (2, 2)

def test_parser_border():
    # no argument k
    # sys.argv = ['test_shingle.py', '-n', '3.5', '-k', '2']
    # with pytest.raises(SystemExit) as e:
    #     parser()
    # assert e.type == SystemExit
    # assert str(e.value) == '2'
    # # no argument n
    # sys.argv = ['test_shingle.py', '-k', '1']
    # with pytest.raises(SystemExit):
    #     parser()
    # # argument type float
    # sys.argv = ['test_shingle.py', '-n', '1.0', '-k', '1']
    # with pytest.raises(SystemExit):
    #     parser()
    # #argument type list
    # sys.argv = ['test_shingle.py', '-n', '[1]', '-k', '1']
    # with pytest.raises(SystemExit):
    #     parser()
    pass
# def test_get_input_typical():
#     input_values = ['']
#     with monkeypatch.context() as m:
#         m.setattr('builtins.input', lambda: input_values.pop(0))
#         result = get_input()
#     assert result == []



