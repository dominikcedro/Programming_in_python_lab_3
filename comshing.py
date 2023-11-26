
from shingle import shingles
from shingle import most_common_shingles



import argparse
from collections import Counter
import string


parser3 = argparse.ArgumentParser(description = 'Compare two text files with Jaccards similarity and find n most common k-shingles in the text file.')
parser3.add_argument('--query', help='Path to the query text file')
parser3.add_argument('--target', help='Path to the target text file')
parser3.add_argument('-k', type=int, required=True, default=1, help='Length of k-shingles')
parser3.add_argument('--remove_punctuation', action='store_true', help='Remove punctuation from the text')
parser3.add_argument('-n', type=int, required=True, default=1, help='Number of most common k-shingles')
args3 = parser3.parse_args()

#open query file
with open(args3.query, 'r') as query_file:
    query = query_file.read()

# open target
with open(args3.target, 'r') as target_file:
    target = target_file.read()

if args3.remove_punctuation: # if somebody uses this remove punctuation option
    query = query.translate(str.maketrans('', '', string.punctuation))
    target = target.translate(str.maketrans('', '', string.punctuation))
# turn query and target into lists of words
query = query.split()
query_shingles = set(shingles(query, args3.k))
target = target.split()
target_shingles = set(shingles(target, args3.k))

# jaccard similarity
jaccard_similarity = len(query_shingles.intersection(target_shingles)) / len(query_shingles.union(target_shingles))
print(f'Jaccard similarity is {jaccard_similarity}')

k = args3.k
shingles_list = get_input()
shingles_list = shingles(shingles_list, k)
n = args3.n
most_common_shingles(shingles_list, n)