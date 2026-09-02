class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        tank = 0
        n = len(gas)

        for i in range(2*n):
            tank += gas[i%n] - cost[i%n]
            if tank < 0:
                tank = 0
                start = (i + 1)

        return start


