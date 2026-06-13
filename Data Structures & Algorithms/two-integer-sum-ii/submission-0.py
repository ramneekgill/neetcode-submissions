class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(numbers)):
            diff = target-numbers[i]
            if diff in dic:
                return [dic[diff],i+1]
            dic[numbers[i]] = i+1
            