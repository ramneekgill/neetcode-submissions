class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = defaultdict(int)
        for let in s1:
            s1_dict[let] += 1
        
        l, r = 0, len(s1)-1
        s2_dict = defaultdict(int)
        for let in s2[l:r+1]:
                s2_dict[let] += 1

        while r < len(s2):
            if s2_dict == s1_dict:
                return True
            s2_dict[s2[l]] -= 1
            if  s2_dict[s2[l]] == 0:
                del s2_dict[s2[l]]
            if (r+1)<len(s2):
                s2_dict[s2[r+1]] += 1
            l+=1
            r+=1
        return False
        
        
        