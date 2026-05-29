import heapq as hp

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1*stones[i]

        hp.heapify(stones)

        while len(stones) > 1:
            s1 = hp.heappop(stones)
            s2 = hp.heappop(stones)
            print(s1, s2)

            if s1 != s2:
                hp.heappush(stones, -1*abs(s1-s2))

        if not stones:
            return 0

        return -1*stones[0]