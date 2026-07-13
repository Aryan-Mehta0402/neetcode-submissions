class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(0, n)]
        total = 0
        for i in range(n):
            for j in range(i, n):
                total += diff[j]
                if total < 0:
                    total = 0
                    i = j+1

            if total >= 0:
                return i
