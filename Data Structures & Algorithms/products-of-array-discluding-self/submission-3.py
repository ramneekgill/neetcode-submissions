class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward_accum = [1]*len(nums)
        for x in range(1,len(nums)):
            forward_accum[x] = forward_accum[x-1] * nums[x-1]
        
        reverse_accum = 1
        for i in range(len(nums)-1,-1,-1):
            forward_accum[i] *= reverse_accum
            reverse_accum *= nums[i]
        return forward_accum







        