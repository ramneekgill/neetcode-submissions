class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)
        for src,dest in tickets:
            adj[src].append(dest)
        
        res = ['JFK']
        def dfs(src):
            if len(tickets)+1 == len(res):
                return True
            if src not in adj:
                return False
            
            tmp = adj[src].copy()
            for i,dest in enumerate(tmp):
                res.append(dest)
                adj[src].pop(i)
                if dfs(dest):
                    return True
                res.pop()
                adj[src].insert(i, dest)
            return False
        dfs('JFK')
        return res




        