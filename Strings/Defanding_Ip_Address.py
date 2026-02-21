# Defanging an Ip Address
    # Time Complexity = O(n)
    # Space complexity = O(n)

class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        for i in range(len(address)):
            if address[i] != ".":
                ans += address[i]
            if address[i] == ".":
                ans += "["
                ans += "."
                ans += "]"
            
        return ans
        
