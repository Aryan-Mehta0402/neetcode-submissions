class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stk = [] 
        res = [0]*len(temp) 

        for i in range(len(temp)):
            if len(stk) == 0:
                stk.append([temp[i], i])
                continue

            while (len(stk) != 0) and (stk[len(stk)-1][0] < temp[i]):
                res[stk[-1][1]] = i - stk[-1][1]
                stk.pop()
                
            stk.append([temp[i], i])
        
        return res
    