class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        larr = [1]*len(nums)
        rarr = [1]*len(nums)
        prod = 1
        for i in range(0,len(nums)):
            prod *= nums[i]
            larr[i] = prod
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            prod *= nums[i]
            rarr[i] = prod
        output = []
        for i in range(len(nums)):
            l,r = 1, 1
            if (i-1) >= 0:
                l = larr[i-1]
            if (i+1) < len(nums):
                r = rarr[i+1]
            output.append(l*r)
        return output

        