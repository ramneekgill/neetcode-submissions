class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        prev = intervals[0]
        res = []
        for start,end in intervals[1:]:
            if prev[1] < start:
                res.append(prev)
                prev = [start, end]
            else:
                prev = [min(prev[0], start), max(prev[1], end)]
        res.append(prev)
        return res

            