class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def intersectPoint(head1, head2):
    
    nodes = set()
    
    temp1 = head1
    while temp1:
        nodes.add(temp1)
        temp1 = temp1.next
    
    temp2 = head2
    while temp2:
        if temp2 in nodes:
            return temp2.data
        temp2 = temp2.next
    
 
    return -1

def inputList(size, v):
    if size == 0:
        return None
    
    head = Node(v[0])
    tail = head
    
    for i in range(1, size):
        tail.next = Node(v[i])
        tail = tail.next
    
    return head

if __name__ == "__main__":
    import random
    
    T = 1  
    
    while T > 0:
        T -= 1
        
        n1, n2, n3 = list(map(int, input().split())) 
      
        
        p = random.randint(0, 2) 
        
        v1, v2, v3 = [],[],[]
        if n1 != 0:
            v1 = list(map(int, input().split()))
        if n2 != 0:
            v2 = list(map(int, input().split()))
        if n3 != 0:
            v3 = list(map(int, input().split()))
        
        head1 = None
        head2 = None
        common = None
        
        if p == 0:
            common = inputList(n3, v3)
            head1 = inputList(n1, v1)
            head2 = inputList(n2, v2)
        elif p == 1:
            head1 = inputList(n1, v1)
            common = inputList(n3, v3)
            head2 = inputList(n2, v2)
        else:
            head1 = inputList(n1, v1)
            head2 = inputList(n2, v2)
            common = inputList(n3, v3)
        
        temp = head1
        while temp and temp.next:
            temp = temp.next
        if temp:
            temp.next = common
        
        temp = head2
        while temp and temp.next:
            temp = temp.next
        if temp:
            temp.next = common
        
        print(intersectPoint(head1, head2))
