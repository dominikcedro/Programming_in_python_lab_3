import argparse
from collections import Counter
import string
from shingles import shingles
def parser_compare():
    parser = argparse.ArgumentParser(description='Compare two text files with Jaccards something') # change it later
    parser.add_argument('--query', help='Path to the query text file')
    parser.add_argument('--target', help='Path to the target text file')
    parser.add_argument('-k', type=int, help='Length of k-shingles')
    parser.add_argument('--remove_punctuation', action='store_true', help='Remove punctuation from the text')
    return parser.parse_args()

def open_files(args):
    #open query file
    with open(args.query, 'r') as query_file:
        query = query_file.read()
    # open target
    with open(args.target, 'r') as target_file:
        target = target_file.read()
    return query, target

def remove_punctuation(query, target, args):
    if args.remove_punctuation: # if somebody uses this remove punctuation option
        query = query.translate(str.maketrans('', '', string.punctuation))
        target = target.translate(str.maketrans('', '', string.punctuation))
    return query, target

def turn_text_to_list(query, target):
    # turn query and target into lists of words
    query = query.split()
    target = target.split()
    return query, target

def turn_to_shingles(query, target, args):
    query_shingles = shingles(query, args.k)
    target_shingles =shingles(target, args.k)
    return query_shingles, target_shingles

def jaccard(query, target):
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
    args = parser_compare()
    query, target = open_files(args)
    query, target = remove_punctuation(query, target, args)
    query, target = turn_text_to_list(query, target)
    query, target = turn_to_shingles(query, target, args)
    similarity = abs(jaccard(query, target))
    print(f"Jaccard similarity is: {similarity}")
if __name__ == "__main__":
    execute_compare()