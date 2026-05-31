class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sol = "("

        def backtrack(op, cl, sol):
            if op == n:
                s = ""
                for i in range(n - cl):
                    s += ")"
                res.append(sol + s)
                return

            if op == cl:
                sol += "("
                backtrack(op+1, cl, sol)
                sol = sol[:-1]
                return

            # we want op >= cl
            # add op
            sol += "("
            backtrack(op+1,cl, sol)
            sol = sol[:-1]
            
            # add cl
            sol += ")"
            backtrack(op,cl+1, sol)
            sol = sol[:-1]

        backtrack(1, 0, sol)
        return res

        
