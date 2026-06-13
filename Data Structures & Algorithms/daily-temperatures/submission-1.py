class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i,temp in enumerate(temperatures):
            j = i+1
            days = 0
            while j < len(temperatures):
                if temp < temperatures[j]:
                    days = j-i
                    break
                j+=1
            res.append(days)
        return res


        