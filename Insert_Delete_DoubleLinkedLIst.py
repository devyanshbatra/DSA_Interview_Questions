def insertNode(head, position, value):
    newNode = Node(value)
    if position == 1:
        newNode.next = head
        if head:
            head.prev = newNode
        return newNode
    current = head
    curr_pos = 1
    while curr_pos < position - 1 and current is not None:
        current = current.next
        curr_pos += 1
    if current is None:
        return head
    newNode.next = current.next
    newNode.prev = current
    if current.next is not None:
        current.next.prev = newNode
    current.next = newNode
    return head

def deleteNode(head, position):
    if head is None:
        return None
    if position == 1:
        newHead = head.next
        if newHead is not None:
            newHead.prev = None
        return newHead
    current = head
    curr_pos = 1
    while curr_pos < position and current is not None:
        current = current.next
        curr_pos += 1
    if current is None:
        return head
    if current.prev:
        current.prev.next = current.next
    if current.next:
        current.next.prev = current.prev
    return head