class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = sum([int(i)**2 for i in str(n)])
        # print(slow)
        # print(fast)
        while fast != slow:
            for i in range(2):
                fast = sum([int(i)**2 for i in str(fast)])
            slow = sum([int(i)**2 for i in str(slow)])
            
        return True if fast == 1 else False
            


        