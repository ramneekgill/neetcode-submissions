class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        win = 0
        for l in range(len(s)):
            chars = set()
            for r in range(l, len(s)):
                if s[r] in chars:
                    break
                chars.add(s[r])
                win = max(win, (r-l)+1)
        return win


        

            



        