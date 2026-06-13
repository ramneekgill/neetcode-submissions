"""
sliding window
total length - most freq character = k
most freq character is tracked with array of 26 so I can loop through the
entire thing often and it only costs O(26)
1. increment right pointer and increment freqency by 1.
2. create function that loops through all 26 elements and returns current highest
freq
3. subtract highest freq from total length and until k goes over limit
4. when k goes over limit increment left and decrement on frequency and
check new highest frequency 
5. Repeat until total length - most freq character < k
6. Repeat incrementing right pointer
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        freq = [0]*26
        l = 0
        for r in range(len(s)):
            idx_r = ord(s[r]) - ord('A')
            freq[idx_r] += 1
            most_freq = self.maxFreq(freq)
            while ((r-l+1)-most_freq) > k:
                idx_l = ord(s[l]) - ord('A')
                freq[idx_l] -= 1
                l+=1
                most_freq = self.maxFreq(freq)
            longest = max(longest, (r-l+1))
        return longest
            

    def maxFreq(self, freq):
        most = 0
        for i in range(26):
            most = max(most, freq[i])
        return most



        