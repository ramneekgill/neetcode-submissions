class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        hm = {}
        intervals.sort()
        i = 0
        min_heap = []
        
        for q in sorted(queries):
            while i<len(intervals) and q >= intervals[i][0]:
                size = (intervals[i][1]-intervals[i][0])+1
                right = intervals[i][1]
                heapq.heappush(min_heap,(size,right))
                i+=1
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            if min_heap:
                hm[q] = min_heap[0][0]
            else:
                hm[q] = -1
            
        output = [hm[q] for q in queries]
        return output

            
        return output

        