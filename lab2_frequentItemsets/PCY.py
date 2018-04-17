import sys
from collections import defaultdict
import itertools

def countPairs(pair,pairs_count):
    pairs_count[pair]+=1

def firstPass(pair,value,items,threshold,folders,folder_num):
    if items[pair[0]] >= threshold and items[pair[1]] >= threshold:
        k = (pair[0] * len(items) + pair[1]) % folder_num
        folders[k]+= value

def secondPass(pair,value,items,threshold,folders,folder_num,pairs):
    i = pair[0]
    j = pair[1]
    if items[i] >= threshold and items[j] >= threshold:
        k = (i * len(items) + j) % folder_num
        if folders[k] >= threshold:
            pairs[pair] += value

src = sys.stdin
baskets_num = int(src.readline())
threshold = float(src.readline()) * baskets_num
folder_num = int(src.readline())
    
folders = [0] * folder_num
baskets = [0] * baskets_num
pairs = defaultdict(int)
items = defaultdict(int)
pair_count = defaultdict(int)

for i in range(baskets_num):
    baskets[i] = [int(x) for x in src.readline().split()]
    for item in baskets[i]:
        items[item] += 1

paired_baskets = [itertools.combinations(b, 2) for b in baskets]

# counting pairs
[countPairs(pair,pair_count) 
    for basket in paired_baskets
        for pair in basket]

# first pass
[firstPass(pair,pair_count[pair],items,threshold,folders,folder_num) 
    for pair in pair_count]

# second pass
[secondPass(pair,pair_count[pair],items,threshold,folders,folder_num,pairs) 
    for pair in pair_count]

sys.stdout.write(str(len(items)*(len(items)-1)/2)+"\n")
sys.stdout.write(str(len(pairs))+"\n")
for pair in sorted(pairs.values(), reverse=True):
    sys.stdout.write(str(pair)+"\n")
