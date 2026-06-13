class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        matches = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i,v in enumerate(t):
                if target[i] == v:
                    matches.add(i)
        return len(matches) == 3

            

        