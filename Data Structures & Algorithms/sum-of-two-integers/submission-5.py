class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b != 0:
            tmp = ((a & b) << 1) & mask
            a = (a^b) & mask
            b = tmp
        max_int = 0x7FFFFFFF
        if a > max_int:
            return ~(a ^ mask)
        return a
        
        
        
        # max_int = 0x7FFFFFFF
        # return a if a < max_int else ~(a ^ mask)