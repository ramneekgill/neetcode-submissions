class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            prevEnd = output[-1][1]
            if prevEnd >= start:
                output[-1][1] = max(end, prevEnd)
            else:
                output.append([start,end])

        return output



            