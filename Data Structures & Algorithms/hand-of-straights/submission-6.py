class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize > 0:
            return False
        
        dic = collections.Counter(hand)

        for n in hand:
            start = n
            while dic[start-1]:
                start-=1
            
            while start <= n:
                while dic[start]:
                    for i in range(start, start+groupSize):
                        if dic[i] == 0:
                            return False
                        dic[i] -= 1
                start += 1
        return True
                    






        