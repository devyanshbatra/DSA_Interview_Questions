class Node:
    def __init__(self, val):
        self.data = val
        self.left = self.right = None

class Solution:
    def isIdentical(self, node1, node2):
        if not node1 or not node2:
            return node1 == node2  # True if both are None, False if one is None
        return (node1.data == node2.data and 
                self.isIdentical(node1.left, node2.left) and 
                self.isIdentical(node1.right, node2.right))

# Creating two identical binary trees
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)

# Checking if trees are identical
solution = Solution()
print("The binary trees are identical." if solution.isIdentical(root1, root2) 
      else "The binary trees are not identical.")
