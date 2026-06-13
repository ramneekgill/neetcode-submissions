class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        def backtrack(arr):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return
            
            for j in range(len(nums)):
                if j in visited:
                    continue
                visited.add(j)
                arr.append(nums[j])
                backtrack(arr)
                arr.pop()
                visited.remove(j)
        
        backtrack([])
        return res

        