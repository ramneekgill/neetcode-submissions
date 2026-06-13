class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        output = []
        for q in queries:
            curr_min = float('inf')
            for start,end in intervals:
                if q >= start and q <= end:
                    size = (end-start+1)
                    curr_min = min(curr_min, size)
            if curr_min == float('inf'):
                curr_min = -1
            output.append(curr_min)
        return output

        