class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seq = set()
        l, r = 0, 0
        longest = 0
        while r < len(s):
            while s[r] in seq:
                seq.remove(s[l])
                l+=1
            seq.add(s[r])
            r+=1
            longest = max(longest, r-l)
            
        return longest


            
