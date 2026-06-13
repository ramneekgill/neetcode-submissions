class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        num = x
        end = abs(n)
        start = 1
        while (end//start) > 1:
            x *= x
            start = start*2
        while start < end:
            x *= num
            start += 1
        if n < 0:
            x = 1/x
        return x