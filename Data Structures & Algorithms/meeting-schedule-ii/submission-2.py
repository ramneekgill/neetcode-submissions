"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        days = 1
        intervals.sort(key=lambda i: i.start)
        min_heap = []
        prev_end = intervals[0].end
        for i in range(1,len(intervals)):
            if intervals[i].start < prev_end:
                if min_heap and min_heap[0] <= intervals[i].start:
                    heapq.heappop(min_heap)
                else:
                    days += 1
                max_end = max(prev_end, intervals[i].end)
                min_end = min(prev_end, intervals[i].end)
                heapq.heappush(min_heap,max_end)
                prev_end = min_end
            else:
                prev_end = intervals[i].end
        return days


        