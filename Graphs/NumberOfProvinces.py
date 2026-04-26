# Number of Provinces (Leetcode 547)
  # Time Complexity = O(N^2)
  # Space Complexity = O(N^2)

class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(node, adj, vis):
            vis[node] += 1
            for city in  adjList[node]:
                if vis[city] == 0:
                    dfs(city, adj, vis)

        n = len(isConnected)
        vis = [0] * n
        
        adjList = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                   adjList[i].append(j)
                   adjList[j].append(i)
        
        # Represented Matrix as Graph

        noOfProvinces = 0
        for province in range(n):
            if vis[province] == 0:
               noOfProvinces += 1
               dfs(province, adjList, vis)
        return noOfProvinces

        # Second way
        # TC : O(N^2)
        # SC : O(N)
      
        n = len(isConnected)
        visited = set()

        def dfs(node):
            for nei in range(n):
                if isConnected[node][nei] == 1 and nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        count = 0

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                count += 1
        
        return count
        

        
