# Reverse Linked List (Leetcode 206)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1st Way
          
          # Time Complexity = O(2n)
          # Space Complexity = O(n)

        temp = head
        st = []

        while temp != None:
            st.append(temp.val)
            temp = temp.next
        
        temp = head

        while temp != None:
            temp.val = st.pop()
            temp = temp.next
        return head

        # 2nd Way

          # Time Complexity = O(n)
          # Space Complexity = O(1)
        
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
