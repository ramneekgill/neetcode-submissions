class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #check if no cycles
        #confirm visited set has length equal to n to confirm all nodes connected
        visited = set()
        adj_list = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
        
        def dfs(node, parent):
            if node in visited:
                #print(node)
                return False
            
            visited.add(node)
            for child in adj_list[node]:
                if child == parent:
                    continue
                if not dfs(child, node):
                    #print(child)
                    return False
            
            return True

        if not dfs(0,-1):
            return False
        return len(visited) == n

        