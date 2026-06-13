class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def dfs(i,j,w1):
            if i==len(w1) and j==len(word2):
                return 0
            elif j==len(word2):
                return len(w1[i:])
            elif i ==len(w1):
                return len(word2[j:])
            elif w1[i] == word2[j]:
                return dfs(i+1,j+1,w1)
            else:
                replace = w1[:i] + word2[j] + w1[i+1:]
                insert = w1[:i] + word2[j] + w1[i:]
                delete = w1[:i] + w1[i+1:]
                return min(1 + dfs(i+1,j+1,insert), 1 + dfs(i,j,delete), 1 + dfs(i+1,j+1,replace))

            

                
        return dfs(0,0,word1)


                
        