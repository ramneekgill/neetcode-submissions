class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        one, two = 1, 2

        for i in range(n-2):
            tmp = two
            two = one+two
            one = tmp
        
        return two
        