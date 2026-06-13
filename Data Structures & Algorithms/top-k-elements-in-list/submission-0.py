class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for x in nums:
            dic[x] += 1

        new_dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}
        return list(new_dic.keys())[0:k]


        