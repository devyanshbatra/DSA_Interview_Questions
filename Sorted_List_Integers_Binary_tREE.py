class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_balanced(self,node=None):
        def check_balance(node):
            if node is None:
                return true,-1
            left_balance,left_height=check_balance(node.left)
            if not left_balance:
                return False, 0
            right_balance,right_height=check_balance(node.right)
            if  not right_balance:
                return False,0
            balanced=abs(left_height-right_height)<=1
            height= 1+max(left_height-right_height)
            return balanced,height
        balanced=check_balance(self.root,node)
    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        result = []
        self._inorder_helper(node, result)
        return result
    
    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)

    def sorted_list_to_bst(self, nums):
        self.root = self.__sorted_list_to_bst(nums, 0, len(nums) - 1)

    def __sorted_list_to_bst(self,num,left,right):
         def sorted_list_to_bst(self, nums):
        self.root = self.__sorted_list_to_bst(nums, 0, len(nums) - 1)

    def __sorted_list_to_bst(self, nums, left, right):
        if left>right:
            return None
        mid=(left+right)//2
        self.root=nums[mid]
        node.left=__sorted_list_to_bst(self,left,mid-1)
        node.right=__sorted_list_to_bst(self,mid+1,right)
        return self.root
        