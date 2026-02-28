# Remove Duplicates from Sorted List (Leetcode 82)
    # Time Complexity = O(N)
    # Space Complexity = O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                temp = curr
                while temp and temp.next and temp.val == temp.next.val:
                    curr = curr.next
                    temp = temp.next
                else:
                    prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next

