class Solution:
    def isMatch(self, s: str, p: str) -> bool:
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
            if j<(len(p)-1) and p[j+1] == '*':
                if p[j] == s[i] or p[j] == '.':
                    return dfs(i+1,j) or dfs(i,j+2)
                elif p[j] != s[i]:
                    return dfs(i,j+2)
            elif s[i] == p[j] or p[j] == '.':
                return dfs(i+1,j+1)
            elif s[i] != p[j]:
                return False
        return dfs(0,0)
        