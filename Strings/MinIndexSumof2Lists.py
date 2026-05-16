# Minimum Index Sum of Two Lists (Leetcode 599)

# brute version
  # Time complexity = O(n + m)
  # Space complexity = O(n + m)

  class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mini = float('inf')
        dict1 = {}
        dict2 = {}
        res = []

        for i,j in enumerate(list1):
            dict1[j] = i
        
        for i, j in enumerate(list2):
            dict2[j] = i
        
        for i in list2:
            if i in dict1 and i in dict2:
                indexSum = dict1[i] + dict2[i]

                while res and mini > indexSum:
                   res.pop()
                
                if indexSum <= mini:
                   mini = indexSum
                   res.append(i)
        
        return res
        
# Optimized version
  # Time complexity = O(n + m)
  # Space complexity = O(n)

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = {name: idx for idx, name in enumerate(list1)}
        mini = float('inf')
        res = []

        for idx, name in enumerate(list2):
            if name in dict1:
                indexSum = idx + dict1[name]

                if indexSum < mini:
                    mini = indexSum
                    res = [name]
                elif indexSum == mini:
                    res.append(name)

        return res
