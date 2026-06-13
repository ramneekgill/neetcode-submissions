class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        hm = collections.defaultdict(int)
        for r in range(len(s)):
            hm[s[r]] += 1
            while hm[s[r]] > 1:
                hm[s[l]] -= 1
                l += 1 
            longest = max(longest, (r-l)+1)
        return longest




        