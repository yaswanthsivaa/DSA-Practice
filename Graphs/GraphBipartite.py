# is Graph Bipartite ? (Leetcode 785)
  # Time Complexity = O(V + E)
  # Time Complexity = O(V)

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        adjList = {i:graph[i] for i in range(n)}
        group = [-1] * n
        
        def dfs(node, color):
            group[node] = color

            for nei in adjList[node]:
                if group[nei] == -1:
                    if dfs(nei, 1 - color) == False:
                        return False
                    
                elif group[nei] == color:
                    return False
            
            return True

        for i in range(n):
            if group[i] == -1:
               if dfs(i, 0) == False:
                  return False
        
        return True

