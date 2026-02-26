# Odd Even Linked List Problem (Leetcode 328)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Brute Force

        # Time Complexity = O(n/2) + O(n/2) + O(n)  
        # Space complexity = O(n)

        arr = []
        odd = head

        while odd and odd.next:
            arr.append(odd.val)
            odd = odd.next.next
        
        if odd : arr.append(odd.val)
        
        even = head.next

        while even and even.next:
            arr.append(even.val)
            even = even.next.next
        
        if even : arr.append(even.val)
        
        temp = head
        for i in arr:
            temp.val = i
            temp = temp.next
        
        return head
        
        # Optimal
      
        # Time Complexity = O(n/2) * 2 
        # Space complexity = O(1)
        
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        evenHead = head.next

        while even and even.next:

            odd.next = odd.next.next
            even.next = even.next.next
            
            odd = odd.next
            even = even.next
        
        odd.next = evenHead

        return head

