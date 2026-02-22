# Design Linked List (Leetcode 707)

   # Time Complexity = get/addAtTail/addAtIndex/deleteAtIndex: O(n), addAtHead: O(1)
   # Space Complexity = O(n) total, O(1) extra per operation
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0     

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        i = 0
        while i != index:
            curr = curr.next
            i += 1
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        new_node = Node(val)
        curr = self.head
        i = 0
        while i != index - 1:
            curr = curr.next
            i += 1

        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            i = 0
            while i != index - 1:
                curr = curr.next
                i += 1

            curr.next = curr.next.next

        self.size -= 1
