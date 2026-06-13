class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sorted_str = str(sorted(s))
            if sorted_str not in res:
                res[sorted_str] = []
            res[sorted_str].append(s)
        return list(res.values())
                    


                
                

        

        

            
        