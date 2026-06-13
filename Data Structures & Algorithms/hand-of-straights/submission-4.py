class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize > 0:
            return False
        dic = collections.defaultdict(int)
        
        for n in hand:
            dic[n] = dic.get(n, 0)+1
        count = len(hand)//groupSize
        for _ in range(count):
            cur_hand = []
            val = 0
            while dic[val] == 0:
                val += 1
            limit = val+groupSize
            while val < limit:
                if dic[val] > 0:
                    dic[val]-=1
                    val+=1
                else:
                    return False
        return True







        