class Solution:
    def reverseBits(self, n: int) -> int:
        shift_val = 31
        new_val = 0
        while n:
            lsb = n&1
            #print(lsb)
            shifted_lsb = lsb << shift_val
            new_val = new_val | shifted_lsb
            shift_val -= 1
            n = n//2
        return new_val
            
        