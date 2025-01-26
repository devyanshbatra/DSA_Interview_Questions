class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
class Linkedlist:
    def __init__(self,value):
    new_node=Node(value)
    self.head=new_node
    self.tail=new_node
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.tail+=1

def intersectionPresent(head1, head2):
    d1 = head1
    d2 = head2
    while d1 != d2:
        d1 = head2 if d1 == None else d1.next
        d2 = head1 if d2 == None else d2.next
    return d1
def printList(head):
    while head.next != None:
        print(head.value, end='->')
        head = head.next
    print(head.value)
    
if __name__ == '__main__':
    head = None
    head = insertNode(head, 1)
    head = insertNode(head, 3)
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 4)
    head1 = head
    head = head.next.next.next
    headSec = None
    headSec = insertNode(headSec, 3)
    head2 = headSec
    headSec.next = head
    print('List1: ', end='')
    printList(head1)
    print('List2: ', end='')
    printList(head2)
    answerNode = intersectionPresent(head1, head2)
    if answerNode == None:
        print('No intersection')
    else:
        print('The intersection point is', answerNode.val)