import sys
from collections import defaultdict

def iterate_nodes(node, iteration):
    if(iteration in node_iterations[node]):
        return node_iterations[node][iteration]
    else:
        r_t1 = 0
        # iterate through incoming nodes
        for j in incoming[node]:
            # trying to avoid expensive function calls
            if iteration-1 in node_iterations[j]:
                r_t1 += node_iterations[j][iteration-1] / degrees[j]
            else:
                r_t1 += iterate_nodes(j, iteration-1) / degrees[j]
        r_t1 *= beta
        r_t1 += leak
        node_iterations[node][iteration] = r_t1
        return r_t1 

graph = defaultdict(list)
node_iterations = defaultdict(dict)
degrees = defaultdict(int)

src = sys.stdin
readline = src.readline
input = readline().split()
n = int(input[0])
beta = float(input[1])
leak = (1-beta)/n
for i in range(n):
    node_iterations[i][0] = 1.0/n
incoming = defaultdict(list)

# reading the input
for i in range(n):
    graph[i] = [int(nod) for nod in readline().split()]
    [incoming[x].append(i) for x in graph[i]]
    degrees[i] = len(graph[i])

# number of queries
q = int(readline())
for _ in range(q):
    [ex_node, iteration] = [int(x) for x in readline().split()]
    r_t = iterate_nodes(ex_node, iteration)
    print('{0:.10f}'.format(r_t))