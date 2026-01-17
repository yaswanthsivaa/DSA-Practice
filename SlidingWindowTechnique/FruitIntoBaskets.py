# Fruit Into Baskets Problem (LC 904)
  # Time Complexity = O(n)
  # Space Complexity = O(1)

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
      maxNumFruts = 0
        left = 0
        right = 0
        tot = 0
        types = dict()

        while right < len(fruits):
            if fruits[right] not in types:
               types[fruits[right]] = 1
            else:
                types[fruits[right]] += 1
            
            tot = tot + 1

            while len(types) > 2:
                types[fruits[left]] -= 1
                tot -= 1

                if types[fruits[left]] == 0:
                    del types[fruits[left]]
                  
                left = left + 1

            maxNumFruts = max(maxNumFruts, tot)
            right = right + 1

        return maxNumFruts
