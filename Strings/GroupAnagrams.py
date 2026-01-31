# Group Anagrams (Leetcode 49)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

      # Brute Force
      
        # Time Complexity = O(n³ log n)
        # Space Complexity = O(n x n) 
          # n = no of strings and 
          # n = size of strings
      
        gas = []
        form = set()

        for i in range(len(strs)):

            ans = []
            first = strs[i]
            fo = "".join(sorted(first))
            if fo in form:
                continue
            ans.append(first)
            for j in range(i+1, len(strs)):
                if fo == "".join(sorted(strs[j])):
                    ans.append(strs[j])
            
            form.add(fo)
            gas.append(ans)


        return gas

      # Optimal Solution
      
        # Time Complexity = O(n log n)
        # Space Complexity = O(n)
      
        frequency = {}

        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in frequency:
                frequency[sortedWord] = [word]
            else:
                frequency[sortedWord].append(word)
        
        return list(frequency.values())
