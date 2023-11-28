"""
For testing the get_input() function, I used discussion below on stackoverflow:
https://stackoverflow.com/questions/63276033/what-is-the-difference-between-using-mock-mock-vs-mock-patch-and-when-to-us

"""
from unittest.mock import patch
import pytest
from shingle import parser, get_input
import sys
from unittest import mock


def test_parser_typical():
    # normal inputs
    sys.argv = ['test_shingle.py', '-n', '1', '-k', '1']
    assert parser() == (1, 1)
    # normal inputs
    sys.argv = ['test_shingle.py', '-n', '2', '-k', '2']
    assert parser() == (2, 2)


def test_parser_border():
    # ivalid -n value
    args = ['-n', 'one', '-k', '1']
    with patch('sys.argv', ['compare.py'] + args):
        with pytest.raises(SystemExit):
            parser()
    pass
    # ivalid -k value
    args = ['-n', '1', '-k', 'a']
    with patch('sys.argv', ['compare.py'] + args):
        with pytest.raises(SystemExit):
            parser()
    pass
    # missing value n
    args = ['-n', '-k', '1']
    with patch('sys.argv', ['compare.py'] + args):
        with pytest.raises(SystemExit):
            parser()
    pass
    # missing value k
    args = ['-n', '1', '-k']
    with patch('sys.argv', ['compare.py'] + args):
        with pytest.raises(SystemExit):
            parser()
    pass


def test_get_input_typical():
    # normal inputs
    with mock.patch('builtins.input', side_effect=['a', 'b', 'c', 'd', '']):
        assert get_input() == ['a', 'b', 'c', 'd']
    # normal inputs
    with mock.patch('builtins.input', side_effect=['a', 'b', 'c', 'd', 'e', '']):
        assert get_input() == ['a', 'b', 'c', 'd', 'e']


def test_get_input_border():
    # empty input
    with mock.patch('builtins.input', side_effect=['']):
        assert get_input() == []
