import argparse
from shingles import shingles
from collections import Counter
import sys


def parser():
    """Parse command line arguments.
    Args:
        None
    Returns:
        n: number of most common shingles to find, default 1
        k: length of k-shingles, default 1
    Raises:
        ValueError: if n or k are not positive integers
    """

    parser = argparse.ArgumentParser(description='Generate and print most common shingles')
    parser.add_argument('-n', type=int, required=True, default=1, help='Number of most common k-shingles')
    parser.add_argument('-k', type=int, required=True, default=1, help='Length of k-shingles')
    args1 = parser.parse_args()
    n, k = args1.n, args1.k
    return n, k


def get_input():
    """Get input text from the command line until an empty line is entered.
    Args:
        None
    Returns:
         text_list: list of lines.
    """
    text_list = []
    while True:
        try:
            line = input().rstrip('\n')
            text_list.append(line)
            if not line:
                break
        except EOFError:  # check if it works
            break
    text_list = ' '.join(text_list).split()
    return text_list


def most_common(shingles_multiset, n):
    """Find n most common shingles in the shingles_list.

        Args:
            shingles_list: list of shingles
            n: number of most common shingles to find
    """
    print(f"The {n} most common shingles are:")
    for shingle, count in shingles_multiset.most_common(n):
        print(f"{shingle} : {count} times")

def shingle_execute():
    """This function executes the shingle.py script to print results.

    Returns:
        None

    """
    n, k = parser()
    list_of_shingles = get_input()
    result_shingles = shingles(list_of_shingles, k)
    most_common(result_shingles, n)

if __name__ == "__main__": # so it can be imported properly
    shingle_execute()



