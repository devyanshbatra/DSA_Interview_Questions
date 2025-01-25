class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def is_palindrome(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements == elements[::-1]

# Example usage
ll = LinkedList()
ll.add_node('r')
ll.add_node('a')
ll.add_node('d')
ll.add_node('a')
ll.add_node('r')

if ll.is_palindrome():
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")
