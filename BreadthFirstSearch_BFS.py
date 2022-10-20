"""
BFS traversal
start from a given source vertex s.
This code represents a directed graph using adjacency list representation.
"""
from collections import defaultdict

class Graph:
    # constructor
    def __init__(self): 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # function to print a BFS of graph
    def BFS(self, s):
 
        # mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
        print("====", (self.graph))
        print("====", max(self.graph))
 
        # create a queue for BFS
        queue = []
 
        # mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # dequeue a vertex from queue and print it.
            s = queue.pop(0)
            print (s, end = " ")
 
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

# driver code
# create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal (starting from vertex 2)")
g.BFS(2)