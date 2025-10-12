class TreeNode:
    def __init__(self, val=0, left= None, right= None):
        self.val= val
        self.left = left
        self.right= right

    @staticmethod
    def convert(nums):
        if not nums:
            return None

        mid= len(nums) // 2
        root= TreeNode(nums[mid])

        root.left = TreeNode.convert(nums[:mid])
        root.right= TreeNode.convert(nums[mid+1:])
        return root
    
def preorder(node):
    if not node:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)

    

num= [-10,-3,0,5,9]
res= TreeNode.convert(num)
print(preorder(res))

        