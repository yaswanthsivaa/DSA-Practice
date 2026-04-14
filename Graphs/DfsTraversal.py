# Graph Dfs Traversal Algorithm
  # Time Complexity = O(N+E)
  # Space Complexity = O(N)
def dfs(node, adj, vis, ans):
  
  vis[node] = 1
  ans.append(node)
  
  for neighbor in adj[node]:
    if vis[neighbor] == 0:
       vis[neighbor] = 1
       dfs(neighbor, adj, vis, ans)
  return ans 
  
n, m = map(int, input("Enter the no.of nodes and edges: ").split())
ans = []
vis = [0] * (n + 1)
adjList = {}
for _ in range(m):
  u, v = map(int, input().split())
  if u not in adjList:
    adjList[u] = []
  
  if v not in adjList:
    adjList[v] = []
  
  adjList[u].append(v)
  adjList[v].append(u)
  
start = 1  
print(dfs(start, adjList, vis, ans))
  
