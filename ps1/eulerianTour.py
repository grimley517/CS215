# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]
import random
def find_eulerian_tour(graph):
    # your code here
    nodes = []
    for tup in graph:
        for part in tup:
            if part not in nodes:
                nodes.append(part)
    tour = rectour([],nodes, graph)
    return []

def rectour(tour, nodes,graph):
    if len(nodes == 1) and (len(graph) == 1) and (tour[-1] == graph[0][0]) and (tour[0] == graph[0][-1]):
        tour.append(graph[0][-1])
        return tour
    else:
        options = []
        for tup in graph:
            options.append(tup[0])
        nnext = random.choice(options)
        tour.append(nnext)
        nodes.remove(nnext)
        routeOpts = []
        for tup in graph:
            if tup[0] == nnext:
                routeOpts.append(tup)
        route = random.choice(routeOpts)
        graph.remove(route)
        return (rectour(tour, nodes, graph))
    
print (find_eulerian_tour([(1, 2), (2, 3), (3, 1)])
