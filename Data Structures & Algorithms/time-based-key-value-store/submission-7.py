class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        ls = self.time_map[key]
        if len(ls) == 0:
            return ""
        l,r = 0, len(ls)-1

        rec = ""
        while l<=r:
            mid = (l+r)//2
            if ls[mid][0] <= timestamp:
                rec = ls[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return rec
        




        # for pr in reversed(self.time_map[key]):
        #     if pr[0] <= timestamp:
        #         return pr[1]
        # return ""
        

            
        
