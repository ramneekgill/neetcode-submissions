class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        for let in s1:
            s1_dict[let] = s1_dict.get(let, 0) + 1
        
        l, r = 0, len(s1)-1
        while r < len(s2):
            s2_dict = {}
            for let in s2[l:r+1]:
                s2_dict[let] = s2_dict.get(let, 0) + 1
            if s2_dict == s1_dict:
                return True
            l+=1
            r+=1
        return False
        
        
        