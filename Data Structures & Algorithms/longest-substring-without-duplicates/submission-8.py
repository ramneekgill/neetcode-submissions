class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = defaultdict(int)
        lp = 0
        win = 0
        for rp in range(len(s)):
            while hm[s[rp]] == 1:
                hm[s[lp]] -= 1
                lp += 1
            hm[s[rp]] += 1
            win = max(win, (rp-lp)+1)
        return win

            



        