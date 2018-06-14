import sys
from decimal import Decimal, ROUND_HALF_UP

src = sys.stdin
[N,M] = [int(x) for x in src.readline().split()]
matrix = []
for i in range(N):
    matrix.append(src.readline().split())
Q = int(src.readline())
for i in range(Q):
    [I,J,T,K] = [int(x) for x in src.readline().split()]
    print(matrix[I-1][J-1])
    if(T == 1):
        print("user-user")
    else:
        print("item-item")
# Decimal(Decimal(x).quantize(Decimal('.001'), rounding=ROUND_HALF_UP))