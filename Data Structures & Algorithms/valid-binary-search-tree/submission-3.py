# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, maxv, minv):
            if not root:
                return True
            
            if not (minv < root.val < maxv):
                return False
            return dfs(root.left, root.val, minv) and dfs(root.right, maxv, root.val)
            
        return dfs(root, float('inf'), float('-inf'))


        