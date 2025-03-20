def rotateRight(head, R):
    if head is None or head.next is None or R == 0:
        return head
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    length = len(nodes)
    R %= length
    if R == 0:
        return head
    newStart = length - R
    nodes[newStart - 1].next = None
    nodes[length - 1].next = head
    return nodes[newStart]