class Solution:
    def test_k(self, piles, k, h):
        i = 0
        for p in piles:
            h -= math.ceil(p/k)
            if h<0:
                return False
        return True
            
        return hrs <= h
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l<r:
            mid = (l+r)//2
            if self.test_k(piles,mid,h):
                r = mid
            else:
                l = mid + 1
        return r


        
        