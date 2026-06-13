class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_ls = {i:[] for i in range(n)}
        for v1,v2 in edges:
            adj_ls[v1].append(v2)
            adj_ls[v2].append(v1)

        visited = set()
        con_count = 0
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for neigh in adj_ls[node]:
                if neigh == parent:
                    continue
                dfs(neigh, node)
            return True
        
        for i in range(n):
            if dfs(i, -1):
                con_count+=1
        return con_count

