import math
import heapq as hp

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # make a tuple as a node 

        arr = []
        res = []

        for i in range(len(points)):
            dist = math.sqrt(points[i][0]**2+points[i][1]**2)
            arr.append([dist, points[i]])

        hp.heapify(arr)
        for i in range(k):
            res.append(hp.heappop(arr)[1])

        return res

