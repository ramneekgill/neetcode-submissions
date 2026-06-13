class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {(len(s),0): True}
        def dfs(i,open_count):
            if open_count<0:
                return False
            if i==len(s):
                return open_count == 0
            if (i,open_count) in dp:
                return dp[(i,open_count)]
            if s[i] == '(':
                dp[(i, open_count)] = dfs(i+1, open_count+1)
            elif s[i] == ')':
                dp[(i, open_count)] = dfs(i+1, open_count-1)
            else:
                dp[(i, open_count)] = (dfs(i+1, open_count+1) or dfs(i+1, open_count-1) or dfs(i+1, open_count))
            return dp[(i, open_count)]
        return dfs(0,0)
        