class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        new_perms = []
        for p in perms:
            for i in range(len(p)+1):
                new_perm = p.copy()
                new_perm.insert(i,nums[0])
                new_perms.append(new_perm)
        return new_perms


        