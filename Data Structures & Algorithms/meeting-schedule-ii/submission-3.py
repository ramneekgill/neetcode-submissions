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
        heapq.heappush(min_heap, intervals[0].end)
        for i in range(1,len(intervals)):
            if min_heap[0] <= intervals[i].start:
                heapq.heappop(min_heap)
            else:
                days += 1
            heapq.heappush(min_heap,intervals[i].end)
        return days


        