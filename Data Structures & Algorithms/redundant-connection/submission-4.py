class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)]

        visited = set()
        def dfs(node, par):
            if node in visited:
                return True
            
            visited.add(node)
            for neigh in adj[node]:
                if neigh == par:
                    continue
                if dfs(neigh, node):
                    return True
            return False
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = set()
            if dfs(u,-1):
                return [u, v]
        return []


            

        