class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinaryTree:
    def __init__(self):
        self.root=None
    def insert(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
        return True
    temp=self.root
    while (true):
        if new_node.value==temp.value:
            return false
        if new_node.value < temp.value:
            if temp.left is None:
                temp.left=new_node
                return True
            temp=temp.left
        else:
            if temp.right is None:
                temp.right=new_node
                return True
            temp=temp.right
    def Preorder(self):
        result=[]

    def traverse(current_node):
        result.append(current_node)
        if current_node.left is not None:
            traverse(current_node.left)
        if current_node.right is not None:
            traverse(current_node.right)
            
    traverse(self.root)
    return(result)


my_tree=BinaryTree()
my_tree.insert(2)
my_tree.insert(3)
my_tree.insert(4)
print(my_tree.Preorder())
    

        
