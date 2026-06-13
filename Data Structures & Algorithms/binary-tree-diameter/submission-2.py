# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxLength = 0
        def dfs(root):
            nonlocal maxLength
            if not root:
                return 0
            leftLength = dfs(root.left) 
            rightLength = dfs(root.right)
            total = leftLength + rightLength
            maxLength = max(total, maxLength)
            return 1 + max(leftLength, rightLength)
        dfs(root)
        return maxLength
        