class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        while l<r:
            while l<r and not self.isAlNum(s[l]):
                l+=1
            while r>l and not self.isAlNum(s[r]):
                r-=1
            if not (s[l].lower() == s[r].lower()):
                return False
            l+=1
            r-=1
        return True
    
    def isAlNum(self, ch):
        return ((ord('A') <= ord(ch) <= ord('Z')) or
        (ord('a') <= ord(ch) <= ord('z')) or (ord(ch) >= ord('0') and ord(ch)<=ord('9')))


        