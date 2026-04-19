# Swap Nodes In Pairs (Leetcode 24)
  # Time Complexity = O(N)
  # Space Complexity = O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        while prev.next and prev.next.next:
            a = prev.next
            b = a.next
            nextNode = b.next

            # swap
            b.next = a
            a.next = nextNode
            prev.next = b

            prev = a
        
        return dummy.next
