class Solution:
    def numTrees(self, n: int) -> int:
        if n < 3:
            return n
        dp = [0] + [False] * n
        dp[1] = 1
        dp[2] = 2
        for idx in range(3, n + 1):
            dp[idx] += 2 * dp[idx - 1]
            i = 1
            j = idx - 2
            while i <= idx - 2 and j >= 1:
                dp[idx] += dp[i] * dp[j]
                i += 1
                j -= 1
        return dp[-1]
