class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinaryTree:
    def __init__(self):
        self.root=None
class Solution:
    def is_balanced(self,root):
        return self.dfsHeight(root) != -1
    def subtree_height(self,root):
        left_subtree=self.subtree_height(root.left)
        if left_subtree ==-1:
            return -1
        right_subtree=self.subtree_height(root.right)
        if right_subtree==-1:
            return -1
        if abs(left_subtree-right_subtree)>=1:
            return -1
        else:
            return max(left_subtree,right_subtree)+1
        root = Node(1)

root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)

solution=Solution()
