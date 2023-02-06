from collections import defaultdict

# class to represent a graph
class Graph:
	def __init__(self, vertices):
		self.graph = defaultdict(list) # dictionary containing adjacency List
		self.V = vertices # No. of vertices

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# a recursive function used by topologicalSort
	def topologicalSortUtil(self, v, visited, stack):

		# mark the current node as visited.
		visited[v] = True

		# recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i] == False:
				self.topologicalSortUtil(i, visited, stack)

		# push current vertex to stack which stores result
		stack.append(v)

	# The function to do Topological Sort.
	# It uses recursive topologicalSortUtil().
	def topologicalSort(self):
		# mark all the vertices as not visited
		visited = [False] * self.V
		stack = []

		# call the recursive helper function to store Topological
		# Sort starting from all vertices one by one.
		for i in range(self.V):
			if visited[i] == False:
				self.topologicalSortUtil(i, visited, stack)

		# print contents of the stack
		print(stack[ : : -1]) # return list in reverse order

# driver Code
if __name__ == '__main__':
	g = Graph(6)
	g.addEdge(5, 2)
	g.addEdge(5, 0)
	g.addEdge(4, 0)
	g.addEdge(4, 1)
	g.addEdge(2, 3)
	g.addEdge(3, 1)

	print("Following is a Topological Sort of the given graph: ")

	# function Call
	g.topologicalSort()
