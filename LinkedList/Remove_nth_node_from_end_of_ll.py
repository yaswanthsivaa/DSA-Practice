# Remove Nth node From End of Linkedlist (Leetcode 19)
  # Time Complexity = O(2n)
  # Space Complexity = O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        size = 0
        curr = head

        while curr:
            curr = curr.next
            size += 1
        
        # Edge case handle it
        if n == size:
            return head.next
        
        curr = head
        count = 0
        while curr:
            if size - n - 1 == count and curr.next:
                curr.next = curr.next.next
                break
            curr = curr.next
            count += 1

        return head
        
        
