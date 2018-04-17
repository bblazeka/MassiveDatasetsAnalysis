import sys
from collections import defaultdict
import itertools

def firstPass(i,j,items,threshold,folders,folder_num):
    if items[i] >= threshold and items[j] >= threshold:
        k = (i * len(items) + j) % folder_num
        folders[k]+=1

def secondPass(pair,items,threshold,folders,folder_num,pairs):
    i = pair[0]
    j = pair[1]
    if items[i] >= threshold and items[j] >= threshold:
        k = (i * len(items) + j) % folder_num
        if folders[k] >= threshold:
            pairs[pair] += 1

src = sys.stdin
baskets_num = int(src.readline())
threshold = float(src.readline()) * baskets_num
folder_num = int(src.readline())
    
folders = [0] * folder_num
baskets = [0] * baskets_num
pairs = defaultdict(int)
items = defaultdict(int)

for i in range(baskets_num):
    baskets[i] = [int(x) for x in src.readline().split()]
    for item in baskets[i]:
        items[item] += 1

paired_baskets = [itertools.combinations(b, 2) for b in baskets]

[firstPass(pair[0],pair[1],items,threshold,folders,folder_num) 
    for basket in paired_baskets
        for pair in basket]
    
[secondPass(pair,items,threshold,folders,folder_num,pairs) 
    for basket in [itertools.combinations(b, 2) for b in baskets]
        for pair in basket]   

sys.stdout.write(str(len(items)*(len(items)-1)/2)+"\n")
sys.stdout.write(str(len(pairs))+"\n")
for pair in sorted(pairs.values(), reverse=True):
    sys.stdout.write(str(pair)+"\n")
