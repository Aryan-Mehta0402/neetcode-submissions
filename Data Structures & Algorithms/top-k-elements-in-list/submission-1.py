import heapq as hp
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return k most frequent elements
        # hash map - O(n) key - number, value - freq
        # build heap on this and extract top element k times

        HashMap = {}
        bucket = [[] for i in range(len(nums)+1)]

        for n in nums:
            HashMap[n] = 1 + HashMap.get(n, 0)

        result = []
        for key, val in HashMap.items():
            result.append((-1*val,key))

        hp.heapify(result)
        ans = []
        for i in range(k):
            val1, key1 = result[0]
            ans.append(key1)
            hp.heappop(result)

        return ans            


