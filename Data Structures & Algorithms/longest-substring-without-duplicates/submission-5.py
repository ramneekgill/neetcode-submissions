class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seq = set()
        l, r = 0, 0
        while r < len(s):
            while s[r] in seq:
                seq.remove(s[l])
                l+=1
            seq.add(s[r])
            r+=1
            longest = max(longest, r-l)
            
        return max(longest, r-l)


            
