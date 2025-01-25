class Node:
    def __init__(self, data, next_node=None):
      
        self.data = data       
      
        self.next = next_node  


def delete_middle(head):
    
    if head is None or head.next is None:
        return None

    # Initialize slow and fast pointers
    slow = head
    fast = head.next.next if head.next else None

    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    slow.next = slow.next.next
    return head

def print_linked_list(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)


print("Original Linked List: ", end="")
print_linked_list(head)

head = delete_middle(head)


print("Updated Linked List: ", end="")
print_linked_list(head)

