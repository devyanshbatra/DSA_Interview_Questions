class Solution:
    def rearrange(self, head):
        if not head or not head.next:
            return head
        evenNodes = []
        oddNodes = []
        current = head
        while current:
            nxt = current.next
            current.next = None
            if current.val % 2 == 0:
                evenNodes.append(current)
            else:
                oddNodes.append(current)
            current = nxt
        newHead = None
        tail = None
        def append_nodes(nodes, newHead, tail):
            for node in nodes:
                if newHead is None:
                    newHead = node
                    tail = node
                else:
                    tail.next = node
                    tail = node
            return newHead, tail
        newHead, tail = append_nodes(evenNodes, newHead, tail)
        newHead, tail = append_nodes(oddNodes, newHead, tail)
        return newHead