                            
from collections import deque, defaultdict

# Node structure for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def findVertical(self, root):
        nodes = defaultdict(lambda: defaultdict(lambda: set()))
        todo = deque([(root, (0, 0))])

        while todo:
            temp, (x, y) = todo.popleft()
            nodes[x][y].add(temp.data)
            if temp.left:
                todo.append((temp.left, (x - 1, y + 1)))

            if temp.right:
                todo.append((temp.right, (x + 1, y + 1)))

        ans = []
        for x, y_vals in nodes.items():
            col = []
            for y, values in y_vals.items():
                
                col.extend(sorted(values))
            ans.append(col)

        return ans

def printResult(result):
    for level in result:
        for node in level:
            print(node, end=" ")
        print()
    print()

if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(10)
    root.left.left.right = Node(5)
    root.left.left.right.right = Node(6)
    root.right = Node(3)
    root.right.right = Node(10)
    root.right.left = Node(9)

    solution = Solution()

    # Get the Vertical traversal
    verticalTraversal = solution.findVertical(root)

    # Print the result
    print("Vertical Traversal: ")
    printResult(verticalTraversal)
                           
                        