class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)

        for st in strs:
            cnt = [0]*26
            for s in st:
                cnt[ord(s) - ord('a')] += 1
            counts[tuple(cnt)].append(st)
        return counts.values()


