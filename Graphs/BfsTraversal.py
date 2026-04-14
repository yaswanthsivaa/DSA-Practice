# Graph Bfs Traversal Algorithm
  # Time Complexity = O(N+K)
  # Space Complexity = O(N)


from collections import deque

n, e = map(int, input('Enter the No.of Nodes and No.of Edges:').split())

adjacencyList = {}
for _ in range(e):
  u,v = map(int, input('Enter the Edges:').split())
  
  if u not in adjacencyList:
     adjacencyList[u] = []
  
  if v not in adjacencyList:
     adjacencyList[v] = []
    
  
  adjacencyList[u].append(v)
  adjacencyList[v].append(u)



# GRAPH REPRESENTATION DONE

visitedArray = [0] * (n+1)
queue = deque([1])
result = []
visitedArray[1] = 1

while queue:
   node = queue.popleft()
   result.append(node)

   for neighbor in adjacencyList.get(node, []):
      if visitedArray[neighbor] != 1:
         queue.append(neighbor)
         visitedArray[neighbor] = 1

print(result)
