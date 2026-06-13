class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
                continue
            prod *= num
        
        
        if zero_count >= 2:
            return [0 for _ in range(len(nums))]
        
        res = []
        if zero_count == 1:
            for num in nums:
                if num == 0:
                    res.append(prod)
                else:
                    res.append(0)
            return res

        for num in nums:
            res.append(prod//num)
            
        return res