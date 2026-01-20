# Permutation in String (LC 567)
  # Time complexity = O(N)
  # Space Complexity = O(1)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        count2 = {}
        for i in range(len(s1)):
            count2[s1[i]] = count2.get(s1[i], 0) + 1
        
        count = {}
        for i in range(len(s1)):
            count[s2[i]] = count.get(s2[i], 0) + 1
        
        if count == count2:
            return True
        
        left = 0
        right = k
        

        while right < len(s2):
            count[s2[right]] = count.get(s2[right], 0) + 1
            count[s2[left]] = count[s2[left]] - 1

            if count[s2[left]] == 0:
               del count[s2[left]]
            
            if count == count2:
                return True
                           
            right += 1
            left += 1
        
        return False
