import sys
import hashlib
from collections import defaultdict

scale = 16 # hexadecimal
num_of_bits = 4
k = 128
b = 8
r = k/b

candidates = defaultdict(list)
hashes = []
member_dict = dict()
hexnum_dict = dict()

src = sys.stdin

def comparehash(first,second,limit):
    dif = 0
    zipper = zip(first,second)
    for tup in zipper:
        if tup[0] != tup[1]:
            dif+=1
            if dif > limit:
                return False
    return True

def process(subject):
    sum = 0
    for el in subject:
        if el == "1":
            sum+=1
        else:
            sum-=1
    if sum >= 0:
        return "1"
    else:
        return "0"

def hex_processing(c):
    if(c not in hexnum_dict):
        # solving the left-side trailing zero problem
        hexnum_dict[c] = str(bin(int(c, scale))[2:].zfill(num_of_bits))
    return hexnum_dict[c]

def word_processing(member,sh):
    if(member not in member_dict):
        hash = hashlib.md5(member.encode('utf-8'))
        member_dict[member] = hash.hexdigest()
    bins = [hex_processing(c) for c in member_dict[member]]
    binary = "".join(bins)
    return binary

def simhash(text):
    sh = [0] * k
    binaries = [word_processing(t,sh) for t in text.split()]
    zipped = zip(*binaries)
    simhash = [process(tup) for tup in zipped]
    # returns binary of a hash
    return "".join(simhash)

def hash2int(belt, inputhash):
    word = inputhash[r*(belt-1):belt*r-1]
    return int(word,2)

def LSH(input_lines):
    # read input lines and convert to hash
    for _ in range(input_lines):
        hashes.append(simhash(src.readline()))
    for belt in range(1,b):
        boxes = {}
        for i in range(len(hashes)):
            intval = hash2int(belt, hashes[i])
            cat_texts = []
            if intval in boxes:
                cat_texts = boxes[intval]
                for txtid in cat_texts:
                    candidates[txtid].append(i)
                    candidates[i].append(txtid)
            else:
                cat_texts = []
            cat_texts.append(i)
            boxes[intval] = cat_texts
            
def main():
    # read number of input lines
    input_lines = int(src.readline())
    LSH(input_lines)
    # read number of queries
    queries = int(src.readline())
    for _ in range(queries):
        query = [int(x) for x in src.readline().split()]
        h = hashes[query[0]]
        diff = query[1]
        cntr = 0
        for ind in candidates[query[0]]:
            if comparehash(h,hashes[ind],diff):
                cntr+=1
        sys.stdout.write(str(cntr)+"\n")

main()
#print(hex(int(simhash("fakultet elektrotehnike i racunarstva"),2)))