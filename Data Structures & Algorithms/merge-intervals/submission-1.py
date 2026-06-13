class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        interval = [intervals[0][0], intervals[0][1]]
        for i in range(1, len(intervals)):
            if interval[1] < intervals[i][0]:
                res.append(interval)
                interval = intervals[i]
            else:
                interval = [interval[0], max(interval[1],intervals[i][1])]
        res.append(interval)
        return res


        