class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            for nei in adj_list[node]:
                if nei == parent:
                    continue
                dfs(nei,node)

        connected = 0
        for i in range(n):
            if i not in visited:
                dfs(i,-1)
                connected += 1
        return connected


        