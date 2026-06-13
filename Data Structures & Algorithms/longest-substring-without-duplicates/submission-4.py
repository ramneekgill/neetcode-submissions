class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seq = set()
        l, r = 0, 0
        while r < len(s):
            if s[r] in seq:
                longest = max(longest, r-l)
                while s[r] in seq:
                    seq.remove(s[l])
                    l+=1
            seq.add(s[r])
            r+=1
        return max(longest, r-l)


            
