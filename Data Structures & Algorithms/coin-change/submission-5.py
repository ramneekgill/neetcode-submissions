class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = float('inf')
        memo = {}
        def backtrack(target, cnt):
            nonlocal res
            if (target,cnt) in memo:
                return memo[(target,cnt)]

            if target == amount:
                res = min(res, cnt)
                return res
            
            if target > amount:
                return float('inf')

            for coin in coins:
                val = backtrack(target+coin, cnt+1)
                if val != float('inf'):
                    memo[(target, cnt)] = val
        backtrack(0,0)
        return res if res != float('inf') else -1