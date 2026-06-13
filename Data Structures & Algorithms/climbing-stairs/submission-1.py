class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        n1 = 1
        n2 = 2
        for _ in range(2,n):
            tmp = n1+n2
            n1 = n2
            n2 = tmp
        return n2
        