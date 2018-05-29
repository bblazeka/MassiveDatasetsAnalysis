import sys
import math
from collections import deque

src = sys.stdin
error_rate = 0.5
timestamp = 0
oldest = -1
# number of buckets of same size
same_buckets = int(math.ceil(1/error_rate))
# window size
N = int(src.readline())
max_index = int(math.ceil(math.log(N)/math.log(2)))
# list of buckets
buckets = [deque() for _ in range(max_index + 1)]

while True:
    line = src.readline().strip('\n')
    # stop if line is empty
    if not line: break

    # respond to query, return count of ones
    if(line[0] == 'q'):
        query = int(line.split(" ")[1])
        sum = 0
        value = 0
        power = 1
        for bucket in buckets:
            length = len(bucket)
            if length>0:
                if (timestamp-bucket[-1]) >= query:
                    if(length == 1):
                        # the block that is too old is only one, stop iterating
                        break
                    if((timestamp-bucket[-2])>=query):
                        # even another block is too old
                        break
                    # other block can remain
                    length = 1
                value = power
                sum += length * value
            power *= 2
        sum -= value
        sum += math.floor(value / 2)
        print(int(sum))

    # chunk processing
    else:
        for c in line:
            timestamp+=1

            # removing buckets out of the windows
            if(oldest >= 0 and (timestamp - oldest) >= N):
                popped = False
                for bucket in reversed(buckets):
                    if len(bucket) > 0 and popped == False:
                        bucket.pop()
                        popped = True
                        oldest = -1
                    if len(bucket) > 0 and popped == True:
                        oldest = bucket[-1]
                        break
            
            # processing ones
            if(c == "1"):
                if(oldest == -1):
                    oldest = timestamp
                carry_over = timestamp
                for bucket in buckets:
                    bucket.appendleft(carry_over)
                    # counting buckets of same size
                    if(len(bucket) <= same_buckets):
                        break
                    # merge last two
                    last = bucket.pop()
                    second_last = bucket.pop()
                    carry_over = second_last
                    if(last == oldest):
                        oldest = second_last
