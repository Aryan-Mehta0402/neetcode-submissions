class Solution:
    def ispal(self, s):            
        return s == s[::-1]
    
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sol = []

        def backtrack(n):
            if n == len(s):
                res.append(sol[:])
                return

            for i in range(n, len(s)):
                if self.ispal(s[n:i+1]):
                    sol.append(s[n:i+1])
                    backtrack(i+1)
                    sol.pop()
        backtrack(0)
        return res
