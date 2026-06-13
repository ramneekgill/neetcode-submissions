class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        adj_list = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            adj_list[crs].append(pre)
        
        def dfs(crs):
            if crs in visited:
                return False
            if adj_list[crs] == []:
                return True

            visited.add(crs)
            for prereq in adj_list[crs]:
                if not dfs(prereq):
                    return False
            visited.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True




        