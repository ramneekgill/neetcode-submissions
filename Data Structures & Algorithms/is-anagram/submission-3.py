class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = collections.Counter(s)
        count_d = collections.Counter(t)
        count_s.subtract(count_d)
        for key, val in count_s.items():
            print(key)
            print(val)
            if val != 0:
                return False
        
        return True