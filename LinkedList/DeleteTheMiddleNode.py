# Delete the Middle Node in the Linked List (Leetcode 2095)
   # Time Complexity = O(2N)
   # Space Complexity = O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head.next:
            head = None
            return head

        count = 0
        temp = head

        while temp:
            count = count + 1
            temp = temp.next
        
        middle = count // 2
        count = 0
        temp = head

        while temp:
            if count == middle - 1:
                temp.next = temp.next.next
            
            count += 1
            temp = temp.next
        
        return head
