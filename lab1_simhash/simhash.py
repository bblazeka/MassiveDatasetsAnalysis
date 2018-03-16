import hashlib

def simhash(text):
    sh = [0] * 128
    scale = 16 ## hexadecimal
    num_of_bits = 4
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
    return hex(int(simhash,2))

print(simhash("fakultet elektrotehnike i racunarstva"))