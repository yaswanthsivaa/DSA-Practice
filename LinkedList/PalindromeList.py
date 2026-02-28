# Palindrome Linked List (Leetcode 234)

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Brute Force
      
        # Time Complexity = O(2N)
        # Space complexity = O(N)

        auxi = []
        curr = head
        
        while curr:
            auxi.append(curr.val)
            curr = curr.next
        

        left = 0
        right = len(auxi) - 1

        while left < right:
            if auxi[left] != auxi[right]:
                return False
            left += 1
            right -= 1
        
        return True

        # slow + fast Pointer Approach
        # Time Complexity = O(3N)
        # Space Complexity = O(1)
      
        slow = speed = head

        while speed and speed.next:
            slow = slow.next
            speed = speed.next.next
        
        
        # Heart of this Code

        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        
        left = head
        right = prev

        while right:
            if left.val != right.val:
               return False
            left = left.next
            right = right.next
        
        return True

        # Slow + Fast and Stack Approach
         # Time Complexity = O(2N)
         # Space Complexity = O(N)
      
        stack = []

        slow = speed = head

        while speed and speed.next:
            stack.append(slow.val)
            slow = slow.next
            speed = speed.next.next
        
        if speed:
            slow = slow.next
        
        curr = slow
        while curr:
            if curr.val != stack.pop():
                return False
            
            curr = curr.next
        
        return True
