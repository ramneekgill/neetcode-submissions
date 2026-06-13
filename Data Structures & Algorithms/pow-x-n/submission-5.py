class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        c = x
        if n < 0:
            x = 1/x
            c = x
            n = abs(n)
        while (n-1):
            x *= c
            n-=1
        return x
        