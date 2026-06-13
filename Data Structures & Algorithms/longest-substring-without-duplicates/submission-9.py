class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        lp = 0
        win = 0
        for rp in range(len(s)):
            if s[rp] in hm:
                lp = max(lp, hm[s[rp]]+1)
            hm[s[rp]] = rp
            win = max(win, (rp-lp)+1)
        return win

            



        