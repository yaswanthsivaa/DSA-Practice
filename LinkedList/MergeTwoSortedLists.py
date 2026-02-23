# Merge Two Sorted Lists (Leetcode 21)
  # Time Complexity = O(n)
  # Space Complextiy = O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        l1 = list1
        l2 = list2
        
        # comparing and attach to Third linked list
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        # If still l1 has nodes then attach rest of nodes to Third list
        if l1:
            tail.next = l1
        
        # If still l2 has nodes then attach rest of nodes to Third list
        if l2:
            tail.next = l2
        
        # Return head of the merged Linked list
        return dummy.next
