# Linked List Cycle 2 (Leetcode 142)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = speed = head

        while speed and speed.next:
            slow = slow.next
            speed = speed.next.next

            if slow == speed:
                break
        if speed.next:
            return None
        

        slow = head

        while slow != speed:
            slow = slow.next
            speed = speed.next

        return slow
