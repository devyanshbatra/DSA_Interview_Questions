class Node:
    def __init__(self,value):
    self.value=ValueError
    self.right=None
    self.left=None
class BinaryTree:
    def __init__(self,value):
        self.root=None
    def insert(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
        temp=self.root
        while (true):
            if new_node.value<temp.value:
                if temp.left is None:
                    temp.left=new_node
                    return True
                else:
                    if temp.right is None:
                    temp.right=new_node
                    return True
                    temp=temp.right
    def BFS(self):
        temp=self.root
        queue=[]
        result=[]
        queue.append(temp)
        while len(queue)>0:
            temp=queue.pop(0)
            result.append(temp.value)
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)
        return result

my_tree=BinaryTree()
my_tree.insert(3)
my_tree.insert(4)
my_tree.insert(5)
print(my_tree.BFS)


