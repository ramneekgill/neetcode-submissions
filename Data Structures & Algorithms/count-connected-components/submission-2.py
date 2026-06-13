class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(n1):
            cur = n1
            while par[cur] != cur:
                par[cur] = par[par[cur]]
                cur = par[cur]
            return cur

        def union(n1,n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            else:
                if rank[p1] > rank[p2]:
                    par[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    par[p1] = p2
                    rank[p2] += rank[p1]
                return 1
        

        for n1,n2 in edges:
            n -= union(n1,n2)
        return n


        