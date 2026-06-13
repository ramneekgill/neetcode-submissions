class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = [0]*26
        for ch in s:
            freq[ord(ch)-ord('a')] += 1
        res = []
        q = set()
        size = 0
        for i in range(len(s)):
            fidx = ord(s[i])-ord('a')
            if freq[fidx] > 1:
                q.add(s[i])
                freq[fidx]-=1
            else:
                if s[i] in q:
                    q.remove(s[i])
                freq[fidx] -= 1
            size += 1
            if len(q) == 0:
                res.append(size)
                size = 0
        return res

            

            

        