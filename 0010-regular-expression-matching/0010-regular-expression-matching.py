class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True 

        for j in range(2, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):  
            for j in range(1, n + 1):

                # Case 1: Current characters match
                if p[j - 1] == s[i - 1] or p[j - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]

                # Case 2: '*' found
                elif p[j - 1] == "*":

                    # Ignore x*
                    dp[i][j] = dp[i][j - 2]

                    # Use x* if previous char matches
                    if p[j - 2] == s[i - 1] or p[j - 2] == ".":
                        dp[i][j] |= dp[i - 1][j]

        return dp[m][n]