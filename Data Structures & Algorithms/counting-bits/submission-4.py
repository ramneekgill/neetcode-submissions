class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        for i in range(1,n+1):
            j = i
            cnt = 0
            while j:
                j &= (j-1)
                cnt+=1
            res[i] = cnt
        return res




        