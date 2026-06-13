class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        res, visited = set(), set()
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or
                (r,c) in visited or board[r][c] not in node.children):
                return
            
            visited.add((r,c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.isEnd:
                res.add(word)
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visited.remove((r,c))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r,c,root,"")
        return list(res)
        
        