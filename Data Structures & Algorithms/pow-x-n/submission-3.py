class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n == 0:
                return 1
            
            res = helper(x, n//2)
            res = res * res
            return res * x if n%2 else res
        res= helper(x,abs(n))
        if n< 0:
            res = 1/res
        return res