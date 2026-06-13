class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        res_dup = set()
        visited = set()
        adj_list = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            adj_list[crs].append(pre)
        
        def dfs(crs):
            if crs in visited:
                return False
            if crs in res_dup:
                return True
            
            visited.add(crs)
            for pre in adj_list[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            res_dup.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
        