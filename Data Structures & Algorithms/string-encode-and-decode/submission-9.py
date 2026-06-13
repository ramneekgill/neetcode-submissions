class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_s = ""
        for s in strs:
            encoded_s += str(len(s)) + '#' + s
        return encoded_s



    def decode(self, s: str) -> List[str]:
        ptr = 0
        res = []
        while ptr < len(s):
            num = ""
            while s[ptr] != '#':
                num += s[ptr]
                ptr += 1
            ptr += 1
            num = int(num)
            res.append(s[ptr:ptr+num])
            ptr = ptr+num
        return res

