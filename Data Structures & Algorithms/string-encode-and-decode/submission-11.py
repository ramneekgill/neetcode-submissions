class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            sz = len(s)
            res.append(str(sz) + '#' + s)
        return ''.join(res)

            

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            sz = int(s[i:j])
            i += (j-i)+1
            res.append(s[i:i+sz])
            i += sz
        return res

