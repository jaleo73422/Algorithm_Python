# function to perform DFS
def dfs(u):
	visited[u] = True # set the vertex as visited
    	
	for i in adj[u]:
		# visit connected vertices
		if not visited[i]:
			dfs(i)

	# push into the stack on complete visit of vertex
	stack.append(u)

# function to check and return if a cycle exists or not
def check_cycle():
	pos = dict() # stores the position of vertex in topological order
	ind = 0

	# Pop all elements from stack
	while (len(stack) != 0):
		pos[stack[-1]] = ind
		tsort.append(stack[-1]) # push element to get topological Order
		ind += 1
		stack.pop()
	
	print("Topological Order: ", tsort)

	for i in range(n):
		for j in adj[i]:
			first = 0 if i not in pos else pos[i]
			second = 0 if j not in pos else pos[j]

			# If parent vertex does not appear first, cycle exists.
			if (first > second):
				return True

			# if tsort.index(i) > tsort.index(j):
			# 	return True

	return False # Return false if cycle does not exist.

# function to add edges from u to v
def addEdge(u, v):
	adj[u].append(v)

# driver Code
if __name__ == "__main__":
	# n = 4
	n = 6
	stack = [] # stack to store the visited vertices in the Topological Sort
	tsort = [] # store Topological Order
	adj = [[] for i in range(n)] # adjacency list to store edges
	visited = [False for i in range(n)]	# to ensure visited vertex

	# insert edges
	# addEdge(0, 1)
	# addEdge(0, 2)
	# addEdge(1, 2)
	# addEdge(2, 0)
	# addEdge(2, 3)
	
	addEdge(5, 2)
	addEdge(5, 0)
	addEdge(4, 0)
	addEdge(4, 1)
	addEdge(2, 3)
	addEdge(3, 1)

	for i in range(n):
		if (visited[i] == False):
			dfs(i)

	# if cycle exist
	if (check_cycle()):
		print('Yes')
	else:
		print('No')