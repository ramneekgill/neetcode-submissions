# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxLength = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            
            leftLength = dfs(root.left) 
            rightLength = dfs(root.right)
            total = leftLength + rightLength
            self.maxLength = max(total, self.maxLength)
            return 1 + max(leftLength, rightLength)
        dfs(root)
        return self.maxLength
        