import heapq as hp

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hsh = {}
        arr = []
        res = []

        # make dict 
        for i in range(len(tasks)):
            hsh[tasks[i]] = 1 + hsh.get(tasks[i], 0)

        for h in hsh:
            arr.append([-1*hsh[h], h])

        hp.heapify(arr) # max heap

        
        while arr:
            inte = []
            cycle = 0

            # do for n+1 next elements
            for _ in range(n+1):
                if not arr:
                    if inte:
                        res.append("None")
                        cycle += 1
                    continue

                ls = hp.heappop(arr)
                res.append(ls[1])
                cycle += 1
                if ls[0] + 1 != 0:
                    inte.append([ls[0] + 1, ls[1]])

            # update the heap based on the new counts after n operations
            for j in range(len(inte)):
                hp.heappush(arr, inte[j])
                
        print(res)
        return len(res)
        
        

        # do the task with most freq then do the next one 
        # need to make a max heap of size 26
        # and keep doing till we hit n or there are no more elements 
        # len(tasks)*log26 operations - O(n)
        # in that case we add none to the res



