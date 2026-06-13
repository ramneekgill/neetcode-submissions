class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        num = x
        for i in range(abs(n)-1):
            x *= num
        if n < 0:
            x = 1/x
        return x