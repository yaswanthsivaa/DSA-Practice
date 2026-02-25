# Add Two Numbers (Leetcode 2)
    # Time Complexity = O(n)
    # Space Complexity = O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0
        while l1 or l2:
            first = l1.val if l1 else 0   
            second = l2.val if l2 else 0

            tot = first + second + carry
            carry = tot // 10
            digit = tot % 10

            tail.next = ListNode(digit)
            tail = tail.next
            if l1:
               l1 = l1.next
            if l2:
               l2 = l2.next
        
        if carry:
            new = ListNode(carry)
            tail.next = new
        
        return dummy.next



        
