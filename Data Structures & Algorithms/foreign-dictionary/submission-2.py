class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
            
        
        visited = set()
        cycle = set()
        res = []
        def dfs(node):
            if node in cycle:
                return True
            if node in visited:
                return False
            cycle.add(node)
            for neighbor in adj[node]:
                if dfs(neighbor):
                    return True
            cycle.remove(node)
            visited.add(node)
            res.append(node)
        
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return ''.join(res)
        