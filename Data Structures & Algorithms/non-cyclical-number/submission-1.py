class Solution:
    def isHappy(self, n: int) -> bool:
        dup = set()
        dup.add(n)
        s = n
        while s != 1:
            #n = sum([int(i)**2 for i in str(n)])
            f = s
            s = 0
            while f != 0:
                s += (f%10)**2
                f = f//10
            if s in dup:
                return False
            dup.add(s)
        return True
            


        