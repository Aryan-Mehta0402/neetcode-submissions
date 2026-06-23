class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # f(i) = sum of f(i-coin) for coin in coins if i >= coin
        dp = {}

        def rec(index, rem):
            if rem == 0:
                return 1
            if rem < 0:
                return 0
            if index == len(coins):
                return 0
            if (index, rem) in dp:
                return dp[(index, rem)]

            dp[(index, rem)] = rec(index, rem - coins[index]) + rec(index+1, rem)
            return dp[(index, rem)]

        return rec(0, amount)
            