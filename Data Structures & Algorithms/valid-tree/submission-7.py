class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_ls = {i:[] for i in range(n)}

        for v1,v2 in edges:
            adj_ls[v1].append(v2)
            adj_ls[v2].append(v1)
        cycle = set()
        print(adj_ls)
        def dfs(node, parent):
            if node in cycle:
                return False
            
            cycle.add(node)
            for neig in adj_ls[node]:
                if neig == parent:
                    continue
                if not dfs(neig, node):
                    return False
            return True
        if not dfs(0,-1):
            return False
        
        return len(cycle) == n