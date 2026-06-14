class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()

        for i in range(len(nums)):
            r = len(nums)-1
            l = i + 1
            while l<r:
                n = nums[i]+nums[l]+nums[r]
                if n == 0:
                    output.add((nums[i],nums[l],nums[r]))
                    l += 1
                    r -= 1
                elif n > 0:
                    r-=1
                else:
                    l+=1
        return list(output)



        