class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def findMaxPathSum(self, root, maxi):
        if root is None:
            return 0
        leftMaxPath = max(0, self.findMaxPathSum(root.left, maxi))
        rightMaxPath = max(0, self.findMaxPathSum(root.right, maxi))
        maxi[0] = max(maxi[0], leftMaxPath + rightMaxPath + root.data)
        return max(leftMaxPath, rightMaxPath) + root.data

    def maxPathSum(self, root):
        maxi = [float('-inf')] 
        self.findMaxPathSum(root, maxi)
        return maxi[0]


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)


solution = Solution()


maxPathSum = solution.maxPathSum(root)
print("Maximum Path Sum:", maxPathSum)
                           