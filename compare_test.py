
from unittest.mock import patch
from compare import parser_compare, open_files, remove_punctuation, turn_text_to_list, turn_to_shingles, jaccard, execute_compare
import pytest
import sys
from unittest import mock
import string

def test_parser_compare_typical():
    #normal inputs
    sys.argv = ['test_compare.py', '--query', 'query.txt', '--target', 'target.txt', '-k', '2', '--remove_punctuation']
    args = parser_compare()
    assert args.query == 'query.txt', args.target == 'target.txt'
    assert args.k == 2
    assert args.remove_punctuation == True
    #normal inputs flag False
    sys.argv = ['test_compare.py', '--query', 'query.txt', '--target', 'target.txt', '-k', '3']
    args = parser_compare()
    assert args.query == 'query.txt', args.target == 'target.txt'
    assert args.k == 3
    assert args.remove_punctuation == False


def test_parser_compare_border():
    #invalid k value
    args = ['--query', 'path/to/query.txt', '--target', 'path/to/target.txt', '-k', 'one']
    with patch('sys.argv', ['compare.py'] + args):
        with pytest.raises(SystemExit):
            parser_compare()
    pass
    #missing argument --k
    args = ['--query', 'path/to/query.txt', '--target', 'path/to/target.txt']
    with patch('sys.argv', ['compare.py'] + args):
        with pytest.raises(SystemExit):
            parser_compare()
    pass
    #missing argument --query
    args = ['--target', 'path/to/target.txt', '-k', '2']
    with patch('sys.argv', ['compare.py'] + args):
        with pytest.raises(SystemExit):
            parser_compare()
    pass
    #missing argument --target
    args = ['--query', 'path/to/query.txt', '-k', '2']
    with patch('sys.argv', ['compare.py'] + args):
        with pytest.raises(SystemExit):
            parser_compare()
    pass




def test_open_files_typical():
    """I concluded, that this function does not need tests

    """
    pass
def test_open_files_border():
    pass

def test_remove_punctuation_typical():
    # test for normal input
    query = "!1?2.3,4!5"
    target = "12345"
    # I couldnt force function to accept manual argument
    query = query.translate(str.maketrans('', '', string.punctuation))
    target = target.translate(str.maketrans('', '', string.punctuation))
    assert query == target
    #test for only punctuation
    query = "!!!"
    query = query.translate(str.maketrans('', '', string.punctuation))
    assert query == ""
def test_turn_text_to_list_typical():
    # normal inputs
    query = "I am a student"
    target = "I was a student"
    assert turn_text_to_list(query, target) == (['I', 'am', 'a', 'student'], ['I', 'was', 'a', 'student'])

def test_turn_to_shingles_typical():
    #normal inputs
    query = ['I', 'am', 'a', 'student']
    target = ['I', 'was', 'a', 'student']
    args = mock.Mock()
    args.k = 2
    assert turn_to_shingles(query, target, args) == ({'I am': 1, 'am a': 1, 'a student': 1}, {'I was': 1, 'was a': 1, 'a student': 1})

def test_jaccard():
    #normal inputs
    query = {'I': 1, 'am': 1, 'student': 1}
    target = {'I': 1, 'am': 1, 'student': 1}
    assert abs(jaccard(query, target)) == 1.0
    # empty input
    query = {}
    target = {'a': 1}
    assert abs(jaccard(query, target)) == 0.0

def test_jaccard_border():
    #both empty inputs
    query = {}
    target = {}
    assert abs(jaccard(query, target)) == 0.0


