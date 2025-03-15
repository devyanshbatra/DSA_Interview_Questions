class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def removeDuplicates(self, head):
        if head is None or head.next is None:
            return head
        current = head
        while current.next is not None:
            if current.data == current.next.data:
                temp = current.next
                current.next = current.next.next
                del temp 
            else:
                current = current.next
        return head