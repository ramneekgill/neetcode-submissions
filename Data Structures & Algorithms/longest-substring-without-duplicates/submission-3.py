class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        longest = 0
        seq = set([s[0]])
        l, r = 0, 1
        while r < len(s):
            if s[r] in seq:
                longest = max(longest, r-l)
                while s[r] in seq:
                    seq.remove(s[l])
                    l+=1
            seq.add(s[r])
            r+=1
        return max(longest, r-l)


            
