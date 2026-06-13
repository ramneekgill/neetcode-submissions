class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for c in range(len(coins)+1)] for r in range(amount+1)]
        for c in range(len(dp[0])):
            dp[0][c] = 1
        
        for r in range(1,len(dp)):
            for c in range(len(dp[0])-2,-1,-1):
                dp[r][c] = dp[r][c+1]
                if (r-coins[c]) >= 0:
                    dp[r][c] += dp[r-coins[c]][c]
        print(dp)
        return dp[len(dp)-1][0]

