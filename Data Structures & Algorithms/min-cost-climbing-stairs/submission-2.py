class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # store cost of reaching top from the ith floor and build a list
        n = len(cost)
        costt = [0]*n
        costt[n-2] = cost[n-2]
        costt[n-1] = cost[n-1]

        for i in range(len(cost) - 3, -1, -1):
            costt[i] = cost[i] + min(costt[i+1], costt[i+2])
        
        print(costt)
        return min(costt[0], costt[1])