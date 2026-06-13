

class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

        
        

    def get(self, key: str, timestamp: int) -> str:
        for x in range(len(self.time_map[key])-1,-1,-1):
            val, prev_timestamp = self.time_map[key][x]
            if prev_timestamp <= timestamp:
                return val
        return ""

        
