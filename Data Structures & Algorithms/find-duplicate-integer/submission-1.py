class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hm = defaultdict(int)
        for n in nums:
            if hm[n] > 0:
                return n
            hm[n] += 1
        return -1
        