class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def countCriticalPoints(head):
    if not head or not head.next or not head.next.next:
        return 0

    count = 0
    prev = head
    cur = head.next
    nxt = cur.next

    while nxt:
        if (cur.val < prev.val and cur.val < nxt.val) or (cur.val > prev.val and cur.val > nxt.val):
            count += 1
        prev = cur
        cur = nxt
        nxt = nxt.next
    return count
head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(2)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(1)

print(countCriticalPoints(head))