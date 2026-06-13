class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_window = float('inf')
        matches = 0
        needed_matches = len(set(t))
        count_t = [0]*52
        count_s = [0]*52
        shortest = ""

        for ch in t:
            if ch.islower():
                count_t[ord(ch)-ord('a')] += 1
            else:
                idx = ord(ch)-ord('A')+26
                count_t[idx] += 1




        l = 0
        for r in range(len(s)):
            idx = 0
            if s[r].islower():
                idx = ord(s[r])-ord('a')
            else:
                idx = ord(s[r])-ord('A') + 26

            count_s[idx] += 1

            if count_s[idx] == count_t[idx]:
                matches+=1
            while matches == needed_matches:
                if (r-l+1) < min_window:
                    min_window = r-l+1
                    shortest = s[l:r+1]

                if s[l].islower():
                    idx = ord(s[l])-ord('a')
                else:
                    idx = ord(s[l])-ord('A') + 26
                count_s[idx] -= 1
                if count_s[idx] == count_t[idx]-1:
                    matches -= 1
                l+=1
            
        return shortest