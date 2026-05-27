class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return k most frequent elements
        # hash map - O(n) key - number, value - freq
        # build heap on this and extract top element k times

        HashMap = {}
        bucket = [[] for i in range(len(nums)+1)]

        for n in nums:
            HashMap[n] = 1 + HashMap.get(n, 0)

        for key, val in HashMap.items():
            bucket[val].append(key)

        res = []
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res

