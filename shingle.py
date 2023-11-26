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
def most_common_shingles(shingles_list, n):
    """Find n most common shingles in the shingles_list.

        Args:
            shingles_list: list of shingles
            n: number of most common shingles to find
    """
    shingles_counter = collections.Counter(shingles_list)
    print(shingles_counter.most_common(n))

k = parser()[1]
shingles_list = get_input()
shingles_list = shingles(shingles_list, k)
n = parser()[0]
most_common_shingles(shingles_list, n)

