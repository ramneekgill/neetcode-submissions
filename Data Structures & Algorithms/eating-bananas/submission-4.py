class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def test_k(k):
            curr_h = 0
            for pile in piles:
                curr_h += math.ceil(pile/k)
            return curr_h
        
        l,r = 1, max(piles)
        while l<r:
            mid = (l+r)//2
            h_val = test_k(mid)
            if(h_val > h):
                l = mid+1
            elif(h_val <= h):
                r = mid
        return r


                


        

        