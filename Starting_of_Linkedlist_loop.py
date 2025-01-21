class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def detect_cycle(head):
    if not head or not head.next:
        return None
    
    # Step 1: Detect if there is a cycle using the Tortoise and Hare approach
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # Cycle detected
            break
    else:
        # If no cycle, return None
        return None

    # Step 2: Find the starting point of the cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # The starting point of the cycle
