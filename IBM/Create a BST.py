class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insertion
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = Node(data)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(data)
                    return
                current = current.right
            
    # Inorder Traversal (Corrected)
    def inorder(self):
        stack = []
        result = []
        current = self.root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left  # ✅ Move to the leftmost node

            current = stack.pop()
            result.append(current.data)  # ✅ Append the node’s **data**, not `current.right`

            current = current.right  # ✅ Move to the right subtree

        return result

# Create BST and insert elements
bst = BST()
bst.insert(10)
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)

# Print the inorder traversal result
print("Inorder Traversal:", bst.inorder())
