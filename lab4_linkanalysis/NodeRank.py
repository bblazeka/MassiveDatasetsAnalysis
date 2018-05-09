import sys

def logic(iter,j):
    basic_node = node_iterations[j]
    previous = basic_node[iter-1]
    try:
        basic_node[iter] += leak
    except IndexError:
        basic_node.append(leak)
    factor = beta * previous / degrees[j]
    connections = graph[j]
    for dest in connections:
        try:
            node_iterations[dest][iter] += factor
        except IndexError:
            node_iterations[dest].append(factor)

def generate_bottom_up():
    [
        logic(i,j)
        for i in range(1,101)
        for j in range(n)
    ]

graph = []
node_iterations = []
degrees = []

src = sys.stdin
readline = src.readline
graph_append = graph.append
degrees_append = degrees.append
node_iters_append = node_iterations.append
input = readline().split()
n = int(input[0])
beta = float(input[1])
leak = (1-beta)/n
for _ in xrange(n):
    node_iters_append([1.0/n])

# reading the input
for i in xrange(n):
    graph_append([int(nod) for nod in readline().split()])
    degrees_append(len(graph[i]))

# generate bottom up
generate_bottom_up()

# number of queries
q = int(readline())
for _ in xrange(q):
    [ex_node, iteration] = [int(x) for x in readline().split()]
    r_t = node_iterations[ex_node][iteration]
    print('{0:.10f}'.format(r_t))