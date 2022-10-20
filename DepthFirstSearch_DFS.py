"""
DFS traversal
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
 
    # a function used by DFS
    def DFSUtil(self, v, visited):
        # mark the current node as visited and print it
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
 
    # the function to do DFS traversal
    # It uses recursive DFSUtil().
    def DFS(self, v):
        # create a set to store visited vertices
        visited = set()

        # call the recursive helper function to print DFS traversal
        self.DFSUtil(v, visited)
 
# driver's code
# create a graph given in the above diagram
if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 
    print("Following is DFS from (starting from vertex 2)")
    # function call
    g.DFS(2)