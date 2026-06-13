class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_sublists = defaultdict(list)
        for s in strs:
            count = [0]*26
            for ch in s:
                count[ord(ch.lower())-ord('a')] += 1
            freq_sublists[tuple(count)].append(s)
        output = []
        for sublist in freq_sublists.values():
            output.append(sublist)
        return output

        
                

        