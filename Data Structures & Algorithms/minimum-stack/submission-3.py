class MinStack:

    def __init__(self):
        self.st = []
        self.curr_min = float('inf')
        

    def push(self, val: int) -> None:
        self.curr_min = min(self.curr_min, val)
        self.st.append([val, self.curr_min])
        

    def pop(self) -> None:
        self.st.pop()

        self.curr_min = self.st[-1][1] if self.st else float('inf')
        

    def top(self) -> int:
        return self.st[-1][0]
        

    def getMin(self) -> int:
        return self.st[-1][1]

        
