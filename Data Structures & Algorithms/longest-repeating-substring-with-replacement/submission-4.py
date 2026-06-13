class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        most_freq = 0
        window = 0
        l = 0
        hm = {}
        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0)+1
            most_freq = max(most_freq, hm[s[r]])
            if (r-l+1)-most_freq > k:
                hm[s[l]] -= 1
                l += 1
            window = max(window, (r-l+1))
        return window   
                

                