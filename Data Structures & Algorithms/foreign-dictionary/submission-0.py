class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        for j in range(len(words)-1):
            w1 = words[j]
            w2 = words[j+1]
            min_len = min(len(w1), len(w2))
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return ""
            for i in range(min_len):
                if w1[i] != w2[i]:
                    adj[w1[i]].add(w2[i])
                    break
            
        visit = {}
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
            
        