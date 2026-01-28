# Remove K Digits (Leetcode  402)
  # Time Complexity = O(N)
  # Space Complexity = O(N)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"

        stack = []
        c = 0

        for i in range(len(num)):
            while stack and stack[-1] > num[i] and c < k:
                stack.pop()
                c += 1
            stack.append(num[i])

        # 🔴 MISSING PART (very important)
        while c < k:
            stack.pop()
            c += 1

        a = "".join(stack)
        aa = a.lstrip("0")

        return aa if aa else "0"
