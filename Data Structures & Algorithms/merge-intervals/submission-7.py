class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev_end = intervals[0][1]
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            if prev_end >= intervals[i][0]:
                prev_end = max(prev_end, intervals[i][1])
                res[-1][1] = prev_end
            else:
                res.append(intervals[i])
                prev_end = intervals[i][1]
        return res


        