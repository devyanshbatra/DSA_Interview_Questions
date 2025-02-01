#Preorder_Traversal
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

    def preordertraversal(root,arr):
        if not root:
            reuturn
            arr.append(root.data)
            preordertraversal(root.left,arr)
            preordertraversal(root.right,arr)
            
    def preorder(root)
        arr=[]
        preordertraversal(root,arr)
        return arr

            
            
