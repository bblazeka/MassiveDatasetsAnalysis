import sys
from collections import defaultdict

def iterate_nodes(node, iteration, node_iters, leak, beta, incoming, degs):
    if(len(node_iters[node]) > iteration):
        return node_iters[node][iteration]
    else:
        r_t1 = 0
        # iterate through incoming nodes
        for j in incoming[node]:
            r_t1 += iterate_nodes(j, iteration-1,node_iters,leak,beta,incoming, degs) / degs[j]
        r_t1 *= beta
        r_t1 += leak
        node_iters[node].append(r_t1)
        return r_t1 

graph = defaultdict(list)
node_iterations = defaultdict(list)
degrees = defaultdict(int)

src = sys.stdin
[n, beta] = src.readline().split()
leak = (1-float(beta))/int(n)
for i in range(int(n)):
    node_iterations[i] = [1/int(n)]
incoming = defaultdict(list)

# reading the input
for i in range(int(n)):
    graph[i] = [int(nod) for nod in src.readline().split()]
    [incoming[x].append(i) for x in graph[i]]
    degrees[i] = len(graph[i])

# number of queries
q = int(src.readline())
for _ in range(q):
    [ex_node, iteration] = [int(x) for x in src.readline().split()]
    r_t = iterate_nodes(ex_node, iteration, node_iterations, leak, float(beta), incoming, degrees)
    print('{0:.10f}'.format(r_t))