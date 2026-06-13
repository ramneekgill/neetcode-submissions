class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i : i[0])
        val = 0
        res = [intervals[0]]
        for start,end in intervals[1:]:
            if start < res[-1][1]:
                val+=1
                if res[-1][1] > end:
                    res.pop()
                    res.append([start,end])
            else:
                res.append([start,end])
        return val
        