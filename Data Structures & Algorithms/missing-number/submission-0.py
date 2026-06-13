class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            s.add(n)

        for i in range(len(nums)+1):
            if i not in s:
                return i
        return -1

        