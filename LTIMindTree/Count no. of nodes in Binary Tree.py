class Tree:
    def __init__(self,value=0,left= None, right= None):
        self.value= value
        self.left= left
        self.right= right 
def count_node(root):
    if root is None:
        return 0
    else:
        return 1+ count_node(root.left) + count_node(root.right)
    

# Constructing the tree
root = Tree(1)
root.left = Tree(2, Tree(4), Tree(5))
root.right = Tree(3, Tree(6), Tree(7))

# Count the nodes
print("Number of nodes:", count_node(root))