import argparse
from shingles import shingles
import collections


parser = argparse.ArgumentParser(description='Generate and print most common shingles')
parser.add_argument('-n', type=int, help='Number of most common k-shingles')
parser.add_argument('-k', type=int, help='Length of k-shingles')
args = parser.parse_args()

text = ''
for line in iter(input, ''):
    text += line

shingles_list = shingles(text, args.k)
shingles_counter = collections.Counter(shingles_list)
most_common = shingles_counter.most_common(args.n)

for shingle, count in most_common:
    print(f"{shingle}: {count} occurrences")