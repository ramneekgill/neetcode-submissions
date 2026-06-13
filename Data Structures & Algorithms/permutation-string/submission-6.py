class Solution:
    def matches(self, freq):
        for val in freq.values():
            if val != 0:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = collections.Counter(s1)
        check = False
        l = 0
        for r in range(len(s2)):
            if s2[r] not in freq:
                while l<=r:
                    if s2[l] in freq:
                        freq[s2[l]] += 1
                    l+=1
                continue
            freq[s2[r]] -= 1
            while freq[s2[r]] < 0:
                freq[s2[l]] += 1
                l += 1
            if self.matches(freq):
                return True
        return False

                    
                    

        #abac

        #aaxbc