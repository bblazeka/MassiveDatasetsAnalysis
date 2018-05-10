import sys

def logic(iter,j):
    previous = iterations[iter-1][j]
    iterations[iter][j] += leak
    factor = beta * previous / degrees[j]
    connections = graph[j]
    for dest in connections:
        iterations[iter][dest] += factor

graph = []
iterations = []
degrees = []

src = sys.stdin
readline = src.readline
graph_append = graph.append
degrees_append = degrees.append
iterations_append = iterations.append
input = readline().split()
n = int(input[0])
beta = float(input[1])
leak = (1-beta)/n
iterations_append([float(1.0/n) for _ in xrange(n)])
for _ in xrange(100):
    iterations_append([0.0 for _ in xrange(n)])

# reading the input
for i in xrange(n):
    graph_append([int(nod) for nod in readline().split()])
    degrees_append(len(graph[i]))

# generate bottom up
[
    logic(i,j)
    for i in xrange(1,101)
    for j in xrange(n)
]

# number of queries
q = int(readline())
for _ in xrange(q):
    [ex_node, iteration] = [int(x) for x in readline().split()]
    r_t = iterations[iteration][ex_node]
    print('{0:.10f}'.format(r_t))