import argparse
from shingles import shingles
import collections

def parser():
    parser = argparse.ArgumentParser(description='Generate and print most common shingles')
    parser.add_argument('-n', type=int, required=True, default=1, help='Number of most common k-shingles')
    parser.add_argument('-k', type=int, required=True,default=1, help='Length of k-shingles')
    args1 = parser.parse_args()
    k = args1.k # delete later
    n = args1.n
    return n, k

def get_input():
    """Get input text from the command line until an empty line is entered.

    Returns:
         text_list: list of lines.
    """
    text_list = []
    while True:
        try:
            line = input()
            if line == '':
                break
            text_list.append(line)
        except EOFError: #check if it works
            break
    del text_list[0] # how to do it more elegant?
    return text_list

k = parser()[1]
shingles_list = get_input()
print(shingles(shingles_list, k))

