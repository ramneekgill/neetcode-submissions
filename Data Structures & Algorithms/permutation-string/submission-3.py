import string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_dict = Counter()
        s2_dict = Counter()
        for i in range (len(s1)):
            s1_dict[s1[i]] += 1
            s2_dict[s2[i]] += 1
        
        matches = 0
        for i in range(ord('a'), ord('z')+1):
            matches += 1 if s1_dict[chr(i)] == s2_dict[chr(i)] else 0
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            s2_dict[s2[r]] += 1
            if s1_dict[s2[r]] == s2_dict[s2[r]]:
                matches += 1
            elif s1_dict[s2[r]] + 1 == s2_dict[s2[r]]:
                matches -= 1

            s2_dict[s2[l]] -= 1
            if s1_dict[s2[l]] == s2_dict[s2[l]]:
                matches += 1
            elif s1_dict[s2[l]] - 1 == s2_dict[s2[l]]:
                matches -= 1
            l += 1
        return matches == 26
            


        
        
        