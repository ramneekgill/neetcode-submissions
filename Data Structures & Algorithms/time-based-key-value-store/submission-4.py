class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if len(self.time_map[key]) <= 0:
            return ""
        for pr in reversed(self.time_map[key]):
            if pr[0] <= timestamp:
                return pr[1]
        return ""
        

            
        
