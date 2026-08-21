class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # store cost of reaching top from the ith floor and build a list
        n = len(cost)
        # costt = [0]*n
        # costt[n-2] = cost[n-2]
        # costt[n-1] = cost

        for i in range(n - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
    
        return min(cost[0], cost[1])