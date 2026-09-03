class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        curr_min = min(val, self.stk[-1][1]) if self.stk else val
        self.stk.append([val, curr_min])

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]
