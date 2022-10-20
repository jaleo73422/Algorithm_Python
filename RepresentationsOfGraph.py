# function to insert vertices to adjacency list
def insert(adj, u, v):
    # insert a vertex v to vertex u
    adj[u].append(v)

    return
 
# function to display adjacency list
def printList(adj, V):
     
    for i in range(V):
        print(i, end = '')
         
        for j in adj[i]:
            print(' --> ' + str(j), end = '')
             
        print()
         
    print()
         
# function to convert adjacency list to adjacency matrix
def convert(adj, V):
    # initialize a matrix
    matrix = [[0 for j in range(V)] for i in range(V)]
     
    for i in range(V):
        for j in adj[i]:
            matrix[i][j] = 1
     
    return matrix

# function to display adjacency matrix
def printMatrix(adj, V):
    
    for i in range(V):
        for j in range(V):
            print(adj[i][j], end = ' ')
            
        print()
        
    print()

# driver code
if __name__=='__main__':
    V = 5

    adjList = [[] for i in range(V)]
  
    # inserting edges
    insert(adjList, 0, 1)
    insert(adjList, 0, 4)
    insert(adjList, 1, 0)
    insert(adjList, 1, 2)
    insert(adjList, 1, 3)
    insert(adjList, 1, 4)
    insert(adjList, 2, 1)
    insert(adjList, 2, 3)
    insert(adjList, 3, 1)
    insert(adjList, 3, 2)
    insert(adjList, 3, 4)
    insert(adjList, 4, 0)
    insert(adjList, 4, 1)
    insert(adjList, 4, 3)
  
    # display adjacency list
    print("Adjacency List: ")
    printList(adjList, V)
  
    # function call which returns adjacency matrix after conversion
    adjMatrix = convert(adjList, V)

    # display adjacency matrix
    print("Adjacency Matrix: ")
    printMatrix(adjMatrix, V)