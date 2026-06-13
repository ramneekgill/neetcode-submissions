class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = collections.Counter(s)
        # count_d = collections.Counter(t)
        # count_s.
        for ch in t:
            # if count_s[ch] == 0:
            #     return False
            count_s[ch] -= 1
        for key, val in count_s.items():
            if val != 0:
                return False
        return True