# Reorder The Linked List (Leetcode 143)
   # Time Complexity = O(n)
   # Space Complexity = O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        curr = head
        arr = []

        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        left = 0
        right = len(arr)-1
        
        curr = head
        
        while curr and left <= right:
            curr.val = arr[left]
            left += 1
            curr = curr.next
        
            if curr and left <= right:
                curr.val = arr[right]
                right -= 1
                curr = curr.next

            



        
