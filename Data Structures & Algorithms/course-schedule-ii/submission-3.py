class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i:[] for i in range(numCourses)}
        visited = set()
        res = []
        for crs,pre in prerequisites:
            adj_list[crs].append(pre)
        
        def dfs(crs):
            if crs in visited:
                return False
            if adj_list[crs] == []:
                return True
            
            visited.add(crs)
            for neig in adj_list[crs]:
                if not dfs(neig):
                    return False
            visited.remove(crs)
            adj_list[crs] = []
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if adj_list[i] == []:
                res.append(i)
        
        for i in range(numCourses):
            if not dfs(i):
                return []
            
            
        return res

        