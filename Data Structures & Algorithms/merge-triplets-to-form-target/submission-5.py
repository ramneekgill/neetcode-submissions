class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr = [-1,-1,-1]
        matches = 0
        for i in range(len(triplets)):
            ls = []
            for j in range(3):
                ls.append(max(curr[j],triplets[i][j]))
            if ls == target:
                return True
            
            ls_matches = sum([1 for x in range(len(target)) if ls[x] == target[x]])
            if ls_matches > matches:
                curr = ls
                matches = ls_matches
        return False

            

        