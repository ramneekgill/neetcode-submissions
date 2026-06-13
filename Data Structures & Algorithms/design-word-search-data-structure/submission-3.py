class PrefixNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = PrefixNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = PrefixNode()
            curr = curr.children[c]
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        def dfs(i, curr):
            for c in range(i, len(word)):
                if word[c] == '.':
                    for child in curr.children:
                        if(dfs(c+1, curr.children[child])):
                            return True
                    return False
                elif word[c] not in curr.children:
                    return False
                curr = curr.children[word[c]]
            return curr.is_end

        curr = self.root
        return dfs(0, curr)
        
