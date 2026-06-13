class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hm = {}
        for i in range(len(s)):
            hm[s[i]] = i
        res = []
        end = 0
        size = 0
        for i in range(len(s)):
            size += 1
            if hm[s[i]] > end:
                end = hm[s[i]]
            if i == end:
                res.append(size)
                size = 0
            
            
        return res
            
                





        