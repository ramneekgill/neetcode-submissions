class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        res = []
        for i in range(len(intervals)):
            if end < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            if start > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]
        res.append(newInterval)
        return res
            
            


        
        

        
        