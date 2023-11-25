import argparse
from collections import Counter
import string
from shingles import shingles
parser = argparse.ArgumentParser(description='Compare two text files with Jaccards something') # change it later
parser.add_argument('--query', help='Path to the query text file')
parser.add_argument('--target', help='Path to the target text file')
parser.add_argument('-k', type=int, help='Length of k-shingles')
parser.add_argument('--remove_punctuation', action='store_true', help='Remove punctuation from the text')
args = parser.parse_args()

#open query file
with open(args.query, 'r') as query_file:
    query = query_file.read()

# open target
with open(args.target, 'r') as target_file:
    target = target_file.read()

if args.remove_punctuation: # if somebody uses this remove punctuation option
    query = query.translate(str.maketrans('', '', string.punctuation))
    target = target.translate(str.maketrans('', '', string.punctuation))
# turn query and target into lists of words
query = query.split()
query_shingles = set(shingles(query, args.k))
target = target.split()
target_shingles = set(shingles(target, args.k))

# jaccard similarity
jaccard_similarity = len(query_shingles.intersection(target_shingles)) / len(query_shingles.union(target_shingles))
print(f'Jaccard similarity is {jaccard_similarity}')