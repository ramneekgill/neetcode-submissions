class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def dfs(i,j):
            if i==len(s) and j==len(p):
                return True
            if j==len(p):
                return False
            if i==len(s):
                if j<(len(p)-1) and p[j+1] == '*':
                    return dfs(i,j+2)
                else:
                    return False
            check = (s[i] == p[j] or p[j] == '.')
            if j<(len(p)-1) and p[j+1] == '*':
                return dfs(i,j+2) or (check and dfs(i+1,j))
            elif check:
                return dfs(i+1,j+1)
            return False
        return dfs(0,0)
        