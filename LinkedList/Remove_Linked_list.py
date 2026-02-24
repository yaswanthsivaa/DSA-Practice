# Remove Linked List (Leetcode 203)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        curr = head

        while curr:

            if curr.val != val:
                tail.next = curr
                tail = tail.next
            
            curr = curr.next
        
        tail.next = None
        return dummy.next
