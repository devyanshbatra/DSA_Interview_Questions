class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
    def delnode(self,N):
        slow=self.head
        fast=self.head

        for fast in range(N):
          fast=fast.next

        if fast is None:
        return head.next
    
        while fast.next is not None:
            slow=slow.next
            fast=fast.next
        dnode=slownext
        slow.next=slow.next.next
        dnode=None

arr = [1, 2, 3, 4, 5]
N = 3
self.head = Node(arr[0])
self.head.next = Node(arr[1])
self.head.next.next = Node(arr[2])
self.head.next.next.next = Node(arr[3])
self.head.next.next.next.next = Node(arr[4])