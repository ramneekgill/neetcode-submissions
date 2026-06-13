# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return [float('-inf'), 0]
            l_m = dfs(node.left)
            r_m = dfs(node.right)
            l_m_w_neg = max(l_m[1], 0)
            r_m_w_neg = max(r_m[1], 0)
            w_split = max(node.val + l_m_w_neg + r_m_w_neg, l_m[0], r_m[0])
            wo_split = node.val + max(l_m_w_neg, r_m_w_neg)
            return [w_split, wo_split]
        return dfs(root)[0]
        