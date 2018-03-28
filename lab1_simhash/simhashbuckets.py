import sys
import hashlib

scale = 16 # hexadecimal
num_of_bits = 4

candidates = {}
hashes = []

def comparehash(first,second,limit):
    dif = 0
    zipper = zip(first,second)
    for tup in zipper:
        if tup[0] != tup[1]:
            dif+=1
            if dif > limit:
                return False
    return True

def simhash(text):
    sh = [0] * 128
    member_dict = dict()
    hexnum_dict = dict()
    members = text.split()
    for member in members:
        binary = ""
        if(member not in member_dict):
            hash = hashlib.md5(member.encode('utf-8'))
            member_dict[member] = hash.hexdigest()
        for c in member_dict[member]:
            if(c not in hexnum_dict):
                # solving the left-side trailing zero problem
                hexnum_dict[c] = bin(int(c, scale))[2:].zfill(num_of_bits)
            binary+=str(hexnum_dict[c])
        i = 0
        for c in binary:
            if c == '1':
                sh[i]+=1
            else:
                sh[i]-=1
            i+=1
    for i in range(0,128):
        if sh[i] >= 0:
            sh[i] = 1
        else:
            sh[i] = 0
    simhash = ''.join(str(x) for x in sh)
    # returns binary of a hash
    return simhash

def hash2int(belt, hash):
    word = hash[belt-1:belt*16]
    return int(word,2)

def LSH(texts):
    k = 128
    b = 8
    r = k/b
    # convert text to hash
    for t in texts:
        hashes.append(simhash(t))
    for belt in range(1,b):
        boxes = {}
        N = len(hashes)
        for id in range(N):
            intval = hash2int(belt, hashes[id])
            cat_texts = {}
            if intval in boxes:
                cat_texts = boxes[intval]
                for txtid in cat_texts:
                    candidates[txtid].append(id)
                    candidates[id].append(txtid)
            else:
                cat_texts.clear()
            
def main():
    texts = []
    src = sys.stdin
    # read number of input lines
    input_lines = int(src.readline())
    # read input lines
    for i in range(0,input_lines):
        texts.append(src.readline())
    LSH(texts)
    # read number of queries
    queries = int(src.readline())
    for i in range(queries):
        query = [int(x) for x in src.readline().split()]
        hash = hashes[query[0]]
        diff = query[1]
        cntr = 0
        for ind in candidates[query[0]]:
            print(hash)
            print(hashes[ind])  
            if comparehash(hash,hashes[ind],diff):
                cntr+=1
        cntr -= 1
        sys.stdout.write(str(cntr)+"\n")

main()
#print(hex(int(simhash("fakultet elektrotehnike i racunarstva"),2)))