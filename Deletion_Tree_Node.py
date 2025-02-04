class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def __r_insert(self,current_node,value):
         if current_node == None: 
            return Node(value)   
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value) 
        return current_node    

    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        self.__r_insert(self.root, value)
    
    def delete_(self,current_node,value):
        if current_node=None:
           return None
        if value<current_node.value:
             current_node.left=self.delete_(current_node.left,value)
        else:
            elif current_node.left==None:
            current_node=current_node.right 
        return current_node
    
    def delete(self.value):
        self.root = self.delete_(self.root, value)
         
    

my_tree = BinarySearchTree()
my_tree.__r_insert(3)
my_tree.__r_insert(4)
my_tree.__r_insert(2)
my_tree.__r_insert(5)
my_tree.__r_insert(1)
my_tree.delete_node(2)



            




        
        
             
