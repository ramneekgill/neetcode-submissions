class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_p = nums.copy()
        running_p = left_p[0]
        left_p[0] = 1
        for i in range(1, len(left_p)):
            tmp = left_p[i]
            left_p[i] = running_p
            running_p *= tmp
        right_p = nums.copy()
        running_p = right_p[len(right_p)-1]
        right_p[len(right_p)-1] = 1
        for i in range(len(right_p)-2, -1, -1):
            tmp = right_p[i]
            right_p[i] = running_p 
            running_p *= tmp
        
        print('left_p: ', left_p)
        print('right_p: ', right_p)
        res = [0]*len(nums)
        for i in range(len(res)):
            res[i] = left_p[i]*right_p[i]
        return res



        