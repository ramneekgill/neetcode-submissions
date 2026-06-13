class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        counter = Counter(hand)
        for x in range(len(hand)//groupSize):
            first_min = min(hand)
            while counter[first_min] == 0:
                first_min+=1
            counter[first_min] -= 1
            for i in range(groupSize-1):
                first_min+=1
                if first_min not in counter or counter[first_min] == 0:
                    return False
                counter[first_min] -= 1
            
        return True

            

        

        