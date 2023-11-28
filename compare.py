import argparse
import string
from shingles import shingles


def parser_compare():
    """Parser for the compare.py script
    Args:
        Arguments are provided from the command line
    Returns:
        parser.parse_args() -- arguments from the command line
        -k -- integer length of k-shingles
        --query -- path to the query text file
        --target -- path to the target text file
        --remove_punctuation -- boolean remove punctuation from the text

    """
    parser = argparse.ArgumentParser(description='Compare two text files with Jaccards similarity')
    parser.add_argument('--query', required=True, help='Path to the query text file')
    parser.add_argument('--target', required=True, help='Path to the target text file')
    parser.add_argument('-k', type=int, required=True, help='Length of k-shingles')
    parser.add_argument('--remove_punctuation', action='store_true', help='Remove punctuation from the text')
    return parser.parse_args()


def open_files(args):
    """

    Args:
        args: arguments from the command line

    Returns:
        query -- query text file as a string
        target -- target text file as a string

    """
    # open query file
    with open(args.query, 'r') as query_file:
        query = query_file.read()
    # open target
    with open(args.target, 'r') as target_file:
        target = target_file.read()
    return query, target


def remove_punctuation(query, target, args):
    """Removed punctuation from the text

    Args:
        query: string of the query text file
        target: string of the target text file
        args: arguments from the command line

    Returns:
        query -- query text file as a string, with no punctuation
        target -- target text file as a string with no punctuation
    """
    if args.remove_punctuation:  # if somebody uses this remove punctuation option
        query = query.translate(str.maketrans('', '', string.punctuation))
        target = target.translate(str.maketrans('', '', string.punctuation))
    return query, target


def turn_text_to_list(query, target):
    """Turns text into lists of words
    Args:
        query: string of the query text file
        target: string of the target text file
    Returns:
        query -- query text file as a list of words
        target -- target text file as a list of words
    """
    # turn query and target into lists of words
    query = query.split()
    target = target.split()
    return query, target


def turn_to_shingles(query, target, args):
    """

    Args:
        query: list of words from the query text file
        target: list of words from the target text file
        args: arguments from the command line

    Returns:
        query_shingles --  list of k-shingles from the query text file
        target_shingles --  list of k-shingles from the target text file
    """
    query_shingles = shingles(query, args.k)
    target_shingles = shingles(target, args.k)
    return query_shingles, target_shingles


def jaccard(query, target):
    """Calculates Jaccard similarity between two texts

    Args:
        query: k-shingles from the query text file
        target: k-shingles from the target text file

    Returns:
        similarity -- float ,Jaccard similarity (roznicka sim) between two texts
    """
    upp = 0
    down = 0
    common_shingles = set(query.keys()) & set(query.keys())
    for key in common_shingles:
        upp += min(query[key], target[key])
        down -= max(query[key], target[key])

    if down == 0:
        return 0.0
    return upp / down


def execute_compare():
    """Executes the compare.py script, prints the result to the console

    """
    args = parser_compare()
    query, target = open_files(args)
    query, target = remove_punctuation(query, target, args)
    query, target = turn_text_to_list(query, target)
    query, target = turn_to_shingles(query, target, args)
    similarity = abs(jaccard(query, target))
    print(f"Jaccard similarity is: {similarity}")


if __name__ == "__main__":
    execute_compare()
