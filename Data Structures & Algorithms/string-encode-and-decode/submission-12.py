class Solution:

    def encode(self, strs: List[str]) -> str:
        f = []
        for s in strs:
            l = len(s)
            f.append(str(l) + '#' + s)
        return ''.join(f)
        
            

    def decode(self, s: str) -> List[str]:
        output = []
        p1, p2 = 0, 0
        while p2 < len(s):
            while s[p2] != '#':
                p2+=1
            val = int(s[p1:p2])
            p1 = p2+1
            s1 = s[p1:p1+val]
            output.append(s1)
            p1 = p2 = p1+val
        return output


            
            
        
