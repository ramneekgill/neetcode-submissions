# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ls = []
        q = [root] if root else None

        while q:
            q_len = len(q)
            sub_ls = []
            for _ in range(q_len):
                node = q.pop(0)
                sub_ls.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ls.append(sub_ls)
        return ls

                
                
            

            
        