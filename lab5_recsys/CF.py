import sys
import numpy as np
import math
from scipy import spatial
from decimal import Decimal, ROUND_HALF_UP

def convert(x):
    try:
        return int(x)
    except:
        return 0

def calculateAverage(index,arrayOfRatings):
    sum = 0
    count = 0
    for member in arrayOfRatings:
        if member > 0:
            sum += member
            count += 1
    return sum * 1.0 / count

def normalize(matrix,averages):
    normalized = []
    for i in range(matrix.shape[0]):
        normalized_row = []
        for j in range(matrix.shape[1]):
            number = matrix[i][j]
            if(number > 0):
                normalized_row.append(number - averages[i] * 1.0)
            else:
                normalized_row.append(0)
        normalized.append(normalized_row)
    return np.array(normalized)

def similar(normalized,row,col):
    similarities = []
    sorted_list = []
    iteration = 0
    for x in range(row):
        similarities.append([])
        for y in range(col):
            x_items = normalized[x]
            y_items = normalized[y]
            try:
                similarities[x].append(float(1.0 - spatial.distance.cosine(x_items, y_items)))
            except:
                similarities[x].append(0)
        sorted_list.append(
            np.asarray((sorted(range(len(similarities[x])),
            key=similarities[x].__getitem__,
            reverse=True))))
        iteration+=1
    return [similarities,sorted_list]


src = sys.stdin
# N items
# M users
[N,M] = [int(x) for x in src.readline().split()]
input_matrix = []
for i in range(N):
    input_matrix.append([convert(x) for x in src.readline().split()])
item_user = np.array(input_matrix)
user_item = item_user.transpose()
item_average = [calculateAverage(x,item_user[x]) for x in range(N)]
user_average = [calculateAverage(x,user_item[x]) for x in range(M)]
# normalize both matrices
item_user_norm = normalize(item_user,item_average)
user_item_norm = normalize(user_item,user_average)
# calculate similarities
[item_user_sim,item_user_order] = similar(item_user_norm,N,M)
[user_item_sim,user_item_order] = similar(user_item_norm,M,N)

Q = int(src.readline())
for i in range(Q):
    [I,J,T,K] = [int(x) for x in src.readline().split()]

    result = 0.0
    if(T == 1):
        # user-user collaborative filtering
        matrix = user_item
        similarities = user_item_sim
        order = user_item_order
        row = J-1
        col = I-1
    else:
        # item-item collaborative filtering
        matrix = item_user
        similarities = item_user_sim
        order = item_user_order
        row = I-1
        col = J-1

    # querying
    counter = 0
    num = 0
    denom = 0
    for other_element in order[row]:
        if(matrix[other_element][col] > 0):
            counter+=1
            num += matrix[other_element][col]*similarities[row][other_element]
            denom += similarities[row][other_element]
        if(counter == K):
            break
    result = num / denom * 1.0

    print(Decimal(Decimal(result).quantize(Decimal('.001'), rounding=ROUND_HALF_UP)))