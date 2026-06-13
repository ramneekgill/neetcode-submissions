class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}
        visited = set()
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
        
        def dfs(crs):
            if crs in visited:
                return False
            if adj_list[crs] == []:
                return True
            
            visited.add(crs)
            for neigh in adj_list[crs]:
                if not dfs(neigh):
                    return False
            
            visited.remove(crs)
            adj_list[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True



        