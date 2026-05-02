# FindIfPathExists (Leetcode 1971)
  # Time Complexity = O(V + E) : we visit each vertex and edge at most once
  # Space Complexity = O(V) : for visited set + recursion stack

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
  
        adj = {}

        for i,j in edges:
            if i not in adj:
                adj[i] = []
            
            if j not in adj:
                adj[j] = []
            
            adj[i].append(j)
            adj[j].append(i)

        vis = set()
        def dfs(vertex):
            
            if vertex == destination:
                return True
            
            vis.add(vertex)
            for ch in adj[vertex]:
                if ch not in vis:
                   if dfs(ch):
                      return True
            
            return False


        return dfs(source)
