# Top K Frequent Elements (Leetcode 347)
  # Time Complexity = O(N log N)
  # Space Complexity = O(K)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = {}
        for i in nums:
            if i not in f:
                f[i] = 0
            else:
                f[i] += 1
                
        sortedItems = sorted(f.items(), key=lambda x:x[1], reverse=True)
        
        return [item[0] for item in sortedItems[:k]]

            
