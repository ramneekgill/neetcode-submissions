class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(arr, i):
            if i >= len(nums):
                res.append(arr.copy())
                return
            for j in range(i, len(nums)+1):
                if j < len(nums):
                    arr.append(nums[j])
                backtrack(arr, j+1)
                if j < len(nums):
                    arr.pop()
        
        backtrack([], 0)
        return res
        