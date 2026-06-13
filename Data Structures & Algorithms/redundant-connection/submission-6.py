class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        def dfs(src, target):
            if src in visited:
                return False
            if src == target:
                return True

            visited.add(src)
            for neighbor in adj[src]:
                if dfs(neighbor, target):
                    return True
            return False

        for u,v in edges:
            visited = set()
            if u in adj and v in adj and dfs(u,v):
                return [u,v]
            adj[u].append(v)
            adj[v].append(u)
        return []