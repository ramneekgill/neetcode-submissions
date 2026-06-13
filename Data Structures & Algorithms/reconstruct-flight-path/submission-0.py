class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_ls = {src: [] for src,dst in tickets}

        tickets.sort()
        for src,dest in tickets:
            adj_ls[src].append(dest)
        
        res = ["JFK"]
        def dfs(src):
            if len(tickets)+1 == len(res):
                return True
            if src not in adj_ls:
                return False
            
            tmp = list(adj_ls[src])
            for i,v in enumerate(tmp):
                adj_ls[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                adj_ls[src].insert(i,v)
                res.pop()
            return False
        dfs("JFK")
        return res
        