class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        highest = 0
        for n in hs:
            cnt = 1
            if (n+1) in hs:
                continue
            while (n-1) in hs:
                cnt +=1
                n -= 1
            highest = max(cnt, highest)
        return highest


        