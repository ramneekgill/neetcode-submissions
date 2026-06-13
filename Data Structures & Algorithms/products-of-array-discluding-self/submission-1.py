class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        num_zeros = 0
        for x in nums:
            if x == 0:
                num_zeros += 1
            else:
                product *= x
        
        res = []
        if num_zeros == 0:
            for x in nums:
                res.append(product//x)
        elif num_zeros == 1:
            for x in nums:
                if x == 0:
                    res.append(product)
                else:
                    res.append(0)
        elif num_zeros > 1:
            for x in nums:
                res.append(0)
        return res

        