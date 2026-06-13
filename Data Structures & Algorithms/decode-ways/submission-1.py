class Solution:
    def numDecodings(self, s: str) -> int:
        res = [0]
        def backtrack(i):
            if i == len(s):
                res[0] += 1
                return
            if s[i] == "0":
                return
            if (i < len(s)-1) and (s[i] == "1" or (s[i] == "2" and int(s[i+1]) <= 6)):
                backtrack(i+2)
            
            backtrack(i+1)
        backtrack(0)
        return res[0]