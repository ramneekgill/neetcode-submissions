# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr_k = 0
        kth_val = -1
        def dfs(root):
            nonlocal curr_k
            nonlocal kth_val
            if not root:
                return None
            dfs(root.left)
            curr_k += 1
            if curr_k == k:
                kth_val = root.val
            dfs(root.right)
        dfs(root)
        return kth_val

            

        