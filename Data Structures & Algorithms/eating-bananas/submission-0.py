import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search on k based on being able to eat bananas in 
        # the given time

        l = 1
        r = 2*max(piles)

        while l < r:
            m = l+(r-l)//2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/m) 
            print(m, hours)
            if hours > h:
                l = m+1
            else:
                r = m
        return l