class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #keep track of most frequent character
        #subtract length of window from most frequent and that value has to be
        #smaller than or equal to k 
        max_window = 0
        for l in range(len(s)):
            most_freq = 1
            freq_ch = s[l]
            hm = defaultdict(int)
            for r in range(l, len(s)):
                hm[s[r]] += 1
                if s[r] in hm and hm[s[r]] > most_freq:
                    freq_ch = s[r]
                    most_freq = max(most_freq, hm[s[r]])
                
                reps = (r-l+1)-most_freq
                if reps > k:
                    break
                max_window = max(max_window, r-l+1)
        return max_window
                