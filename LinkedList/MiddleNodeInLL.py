# Middle Node in Linked List (Leetcode 876)
   # Time Complexity = O(2n)
   # Space Complexity = O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        curr = head

        while curr:
            curr = curr.next
            count += 1
        
        mid = count // 2
        count = 0
        curr = head

        while count < mid:
            curr = curr.next
            count += 1
        
        return curr
            



                    
