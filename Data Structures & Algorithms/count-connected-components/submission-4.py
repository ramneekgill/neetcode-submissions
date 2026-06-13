class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for v1,v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                dfs(neighbor, node)
            return True
        count = 0
        for i in range(n):
            if dfs(i, -1):
                count +=1
        return count

            

