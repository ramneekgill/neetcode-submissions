# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0

            l_h = dfs(root.left)
            r_h = dfs(root.right)
            if abs(l_h-r_h) > 1:
                self.balanced = False
            return 1+max(l_h,r_h)
        dfs(root)
        return self.balanced
        
        