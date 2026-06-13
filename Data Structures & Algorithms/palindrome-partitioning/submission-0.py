class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for c in range(i,len(s)):
                if self.ispali(s, i, c):
                    part.append(s[i:c+1])
                    dfs(c+1)
                    part.pop()
        dfs(0)
        return res

    def ispali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True



        