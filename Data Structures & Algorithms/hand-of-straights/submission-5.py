class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize > 0:
            return False
        hand.sort()
        dic = collections.Counter(hand)
        for n in hand:
            if dic[n]:
                for i in range(n, n+groupSize):
                    if not dic[i]:
                        return False
                    dic[i] -= 1

        return True





        