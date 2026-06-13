class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seq = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in seq:
                seq.remove(s[l])
                l+=1
            seq.add(s[r])
            longest = max(longest, r-l+1)
        return longest


            
