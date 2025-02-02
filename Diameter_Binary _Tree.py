class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinaryTree:
    def __init__(self):
        self.root=None
class Solution:
    def diameter(self,root):
        d=[0]
        self.height(root,d)
        return d[0]
    def search(self,node,d)
        if self.root is None:
            return 0
        lh=self.height(node.left,d)
        rh=self.height(nde.right,d)
        d[0]=max(d[0],lh+rh)
        return 1+(maxlh+rh)
    
if __name__ == "__main__":
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)

    solution = Solution()
    
    diameter = solution.diameterOfBinaryTree(root)
        