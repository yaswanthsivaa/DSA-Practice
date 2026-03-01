# Reverse Nodes in K Groups
   # Time Complexity = O(N)
   # Space Complexity = O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        groupPrev = dummy

        while True:

            kth = groupPrev

            for _ in range(k): # mistake
                kth = kth.next
                if not kth:
                    return dummy.next
            
            nextGroup = kth.next

            # Reverse group
            curr = groupPrev.next
            prev = nextGroup

            while curr != nextGroup:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            # Reconnect
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
    
        return head




                



