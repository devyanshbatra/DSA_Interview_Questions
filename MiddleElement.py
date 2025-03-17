class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def getMiddleElement(head):
    fast=self.head
    slow=fast
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow.data