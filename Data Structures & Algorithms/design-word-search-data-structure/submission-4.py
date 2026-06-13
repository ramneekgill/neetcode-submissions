class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True
        

    def search(self, word: str) -> bool:
        def dfs(i, root):
            for j in range(i, len(word)):
                c = word[j]
                if c == '.':
                    for node in root.children.values():
                        if dfs(j+1, node):
                            return True
                    return False

                else:
                    if c not in root.children:
                        return False
                    root = root.children[c]
            return root.isEnd
        return dfs(0, self.root)


        
