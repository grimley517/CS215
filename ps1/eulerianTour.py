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
    nodes = graph.keys()
    tour = nodes[:]
    print (tour)
    while testTour(graph,tour) != 0:
        tour = nodes[:]
        random.shuffle(tour)
        print (tour)
        tour.append(tour[0])
    return tour

def testTour(graph, tour):
    if not len(graph.keys()) == len(tour)-1:
        return 1
    if not tour[0] == tour[-1]:
        return 2
    for i in range(len(tour)):
        if i < len(tour)-1:
            if tour[i+1] not in graph[tour[i]]:
                return 3
    return 0

def makeGraph(linkTupleList):
    graph = {}
    for link in linkTupleList:
        for node in link:
            if node not in graph.keys():
                graph[node] = []
    for link in linkTupleList:
        graph = addLink(graph, link)
    return graph
        
def addLink (graph, link):
    graph[link[0]].append(link[1])
    graph[link[1]].append(link[0])
    return graph

#G1 = [(1,2), (2,3),(3,4),(2,4),(4,1)]
#print (makeGraph(G1))
#print (testTour(makeGraph(G1),[1,2,3,1]))#should be disconnected, and too short
#print (testTour(makeGraph(G1),[1,2,3,4,1]))
#print (find_eulerian_tour(makeGraph(G1)))
