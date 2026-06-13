class Solution:
    def isHappy(self, n: int) -> bool:
        dup = set()
        dup.add(n)
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            if n in dup:
                return False
            dup.add(n)
        return True
            


        