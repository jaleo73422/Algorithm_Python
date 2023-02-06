# function to add edges from u to v
def addEdge(u, v):
	adj[u].append(v)

# function to perform DFS
def dfs(u):
	visited[u] = True # set the vertex as visited
    	
	for i in adj[u]:
		# visit connected vertices
		if not visited[i]:
			dfs(i)

	# push into the stack on complete visit of vertex
	stack.append(u)

# driver Code
if __name__ == "__main__":
	# n = 4
	n = 6
	stack = [] # stack to store the visited vertices in the Topological Sort
	adj = [[] for i in range(n)] # adjacency list to store edges
	visited = [False for i in range(n)]	# to ensure visited vertex
	
	addEdge(5, 2)
	addEdge(5, 0)
	addEdge(4, 0)
	addEdge(4, 1)
	addEdge(2, 3)
	addEdge(3, 1)

	for i in range(n):
		if (visited[i] == False):
			dfs(i)

	stack.reverse()
	print(stack)