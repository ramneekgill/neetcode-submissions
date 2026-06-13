class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(arr, i):
            for j in range(i, len(nums)+1):
                if j>=len(nums):
                    res.append(arr.copy())
                    break
                arr.append(nums[j])
                backtrack(arr, j+1)
                arr.pop()
        
        backtrack([], 0)
        return res
        