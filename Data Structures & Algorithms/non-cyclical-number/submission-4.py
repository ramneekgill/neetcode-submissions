class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.ssd(n)
        while fast != slow:
            for i in range(2):
                fast = self.ssd(fast)
            slow = self.ssd(slow)
            
        return True if fast == 1 else False
            
    def ssd(self,n):
        return sum([int(i)**2 for i in str(n)])

        