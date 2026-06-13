# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ls = []
        def dfs(node):
            if not node:
                return ls.append('N')
                return
            ls.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(ls)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        ls = data.split(',')
        self.i = 0
        def dfs():
            if ls[self.i] == "N":
                self.i+=1
                return None
            node = TreeNode(int(ls[self.i]))
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

