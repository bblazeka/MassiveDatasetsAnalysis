import sys
from collections import defaultdict

def logic(iter,j):
    basic_node = node_iterations[j]
    try:
        node_iterations[j][iter] += leak
    except IndexError:
        basic_node.append(leak)
    deg = degrees[j]
    for dest in graph[j]:
        try:
            node_iterations[dest][iter] += beta * basic_node[iter-1] / deg
        except IndexError:
            node_iterations[dest].append(beta * basic_node[iter-1] / deg)

def generate_bottom_up():
    [
        logic(i,j)
        for i in range(1,101)
        for j in range(n)
    ]

graph = defaultdict(list)
node_iterations = defaultdict(list)
degrees = defaultdict(int)

src = sys.stdin
readline = src.readline
input = readline().split()
n = int(input[0])
beta = float(input[1])
leak = (1-beta)/n
for i in range(n):
    node_iterations[i] = [1.0/n]

# reading the input
for i in range(n):
    graph[i] = [int(nod) for nod in readline().split()]
    degrees[i] = len(graph[i])

# generate bottom up
generate_bottom_up()

# number of queries
q = int(readline())
for _ in range(q):
    [ex_node, iteration] = [int(x) for x in readline().split()]
    r_t = node_iterations[ex_node][iteration]
    print('{0:.10f}'.format(r_t))