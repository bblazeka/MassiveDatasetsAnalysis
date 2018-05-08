import sys

# BFS
def bfs_shortest_path(graph, start):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
    index = 100000
    min_path = 100000
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            try:
                neighbours = sorted(graph[node])
                # go through all neighbour nodes, construct a new path and push it into the queue
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                
                # mark node as explored
                explored.append(node)
            except KeyError:
                # started on a black node
                if(len(path) == 1):
                    return str(node)+" 0"
                try:
                    dist = len(path)-1
                    if(dist < min_path):
                        min_path = dist
                        index = node
                    elif(dist == min_path and node < index):
                        index = node
                    elif(dist > min_path):
                        return str(index)+" "+str(min_path)
                except:
                    min_path = len(path)-1
                    index = node
    if(index != 100000 or min_path != 100000):
        return str(index)+" "+str(min_path)
    return "-1 -1"

src = sys.stdin
black = []
transitions = {}
[nodes, edges] = [int(x) for x in src.readline().split()]
for i in range(nodes):
    typ = int(src.readline())
    if typ == 0:
        # don't initialize list of transitions
        transitions[i] = list()

# define edges
for _ in range(edges):
    [start, dest] = [int(x) for x in src.readline().split()]
    try:
        transitions[start].append(dest)
    except KeyError:
        err = 1
    try:
        transitions[dest].append(start)
    except KeyError:
        err = 1

# find closest black node
for i in range(nodes):
    # if it is black, write it's index and distance zero
    print(bfs_shortest_path(transitions,i))