class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        res, visited = set(), set()

        for w in words:
            root.insert(w)


        def dfs(r, c, word, node):
            if (r < 0 or c < 0 or r==len(board) or c==len(board[0])
                or (r,c) in visited or board[r][c] not in node.children):
                return
            
            visited.add((r,c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.is_word:
                res.add(word)
            
            dfs(r+1,c,word,node)
            dfs(r-1,c,word,node)
            dfs(r,c+1,word,node)
            dfs(r,c-1,word,node)
            visited.remove((r,c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r,c,"",root)
        return list(res)




        