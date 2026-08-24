class Solution:
    def numDecodings(self, s: str) -> int:
        mapp = {
            "1": "A", "2": "B",
            "3": "C", "4": "D",
            "5": "E", "6": "F",
            "7": "G", "8": "H",
            "9": "I", "10": "J",
            "11": "K", "12": "L",
            "13": "M", "14": "N",
            "15": "O", "16": "P",
            "17": "Q", "18": "R",
            "19": "S", "20": "T",
            "21": "U", "22": "V",
            "23": "W", "24": "X",
            "25": "Y", "26": "Z"
        }

        n = len(s)

        # Empty string or string starting with 0
        if n == 0 or s[0] == "0":
            return 0

        if n == 1:
            return 1

        # dp[i] = number of ways to decode s[i:]
        dp = [0] * n

        # Last character
        if s[n - 1] in mapp:
            dp[n - 1] = 1

        # Last two characters
        if s[n - 2:n] in mapp:
            # Two-digit decoding
            dp[n - 2] += 1

        # Single-digit decoding
        if s[n - 2] in mapp:
            dp[n - 2] += dp[n - 1]

        # Fill DP from right to left
        for i in range(n - 3, -1, -1):

            # Cannot decode a string starting with 0
            if s[i] == "0":
                dp[i] = 0
                continue

            # Decode one digit
            dp[i] = dp[i + 1]

            # Decode two digits
            if s[i:i + 2] in mapp:
                dp[i] += dp[i + 2]

        return dp[0]