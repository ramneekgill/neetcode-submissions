class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] <= intervals[i][1]:
                start = min(newInterval[0], intervals[i][0])
                end = max(newInterval[1], intervals[i][1])
                newInterval = [start, end]
            else:
                res.append(intervals[i])
        res.append(newInterval)
        return res
        

        