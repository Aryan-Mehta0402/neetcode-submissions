class TimeMap:

    def __init__(self):
        self.dicti = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dicti:
            self.dicti[key] = []

        self.dicti[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dicti:
            return ""
        
        l, r = 0, len(self.dicti[key])-1

        while l <= r:
            m = l+(r-l)//2
            if timestamp == self.dicti[key][m][0]:
                return self.dicti[key][m][-1]
            elif timestamp > self.dicti[key][m][0]:
                l = m+1
            else:
                r = m-1
        if timestamp < self.dicti[key][r][0]:
            return ""
        else:
            return self.dicti[key][r][1]
        