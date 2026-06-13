class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()
        while n != 1:
            total = 0
            d = n
            while d != 0:
                digit = d%10
                total += digit**2
                d = d//10
            if total in check:
                return False
            n = total
            check.add(total)
        return True


        