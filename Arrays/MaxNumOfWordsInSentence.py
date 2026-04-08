# Maximum Number of Words Found in Sentence (Leetcode 2114)
   # Time Complexity = O(N)
   # Space Complexity = O(N)

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # Brute Force
        # Time Complexity = O(N.M)
        # Space Complexity = O(N)
      
        ans = 0

        for s in sentences:
            splittedSentence = s.split()
            ans = max(ans, len(splittedSentence))
        
        return ans

        # Optimal Solutions 
      
        # First Way

        # Time Complexity = O(N.M)
        # Space Complexity = O(1)

        for s in sentences:
           
            wordCount = 0
            for w in s:
                if w == " " and wordCount == 0:
                    wordCount += 1
    
            ans = max(wordCount+1, ans)
        
        return ans

        # second Way

        # Time Complexity = O(N.M)
        # Space Complexity = O(N)

        for s in sentences:
            wordCount = 0
            in_word = False

            for ch in s:
                if ch != " " and not in_word:
                    wordCount = wordCount + 1
                    in_word = True
                elif ch == " ":
                    in_word = False
            
            ans = max(ans, wordCount)

        return ans
