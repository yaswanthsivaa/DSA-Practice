# Keys and Rooms (Leetcode 841)
  
  # Breadth First Search
  # Time Complexity = O(N + E)
  # Space Complexity = O(N)

from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        Queue = deque([0])
        visited = set()

        while Queue:
            room = Queue.popleft()
            if room not in visited:
               visited.add(room)
            
               for i in rooms[room]:
                   if i not in visited:
                      Queue.append(i)
        
        return len(visited) == len(rooms)


        # Depth First Search 
        # Time and Space Complexities are same
      
        def dfs(room):
            visited.add(room)

            for i in rooms[room]:
                if i not in visited:
                   dfs(i)

        dfs(0)
        return len(visited) == len(rooms)
        

            


