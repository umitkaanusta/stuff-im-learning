class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if 1 in (m, n):
            return 1
        dp = [[0 for _ in range(n)] for _ in range(m)] #mxn matrix
        # make bottom row 1, including the "finish" square
        for col in range(n):
            dp[m - 1][col] = 1
        # make the rightmost column 1
        for row in range(m):
            dp[row][n - 1] = 1
        for row in range(m - 2, -1, -1):
            for col in range(n - 2, -1, -1):
                dp[row][col] = dp[row + 1][col] + dp[row][col + 1]
        return dp[0][0]
