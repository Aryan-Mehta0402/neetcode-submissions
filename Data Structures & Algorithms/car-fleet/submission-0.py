class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        # calculate time 
        stk_pt = []
        for i in range(len(pos)):
            time = (target-pos[i])/speed[i]
            stk_pt.append([pos[i], time])

        stk_pt.sort()
        # sort a list of lists based on posn 
        stk_t = []
        for i in range(len(stk_pt)):
            stk_t.append(stk_pt[i][1])
       
        # start a pass from right most 
        fleet = 1
        r = stk_t[-1]
        for i in range(len(stk_t)-1, -1, -1):
            if stk_t[i] > r:
                fleet += 1
                r = stk_t[i]
        return fleet
        # if new element is faster then rightmost then pop and add 
        # to fleet count else stop the fleet count
        # keep doing this till end of stk