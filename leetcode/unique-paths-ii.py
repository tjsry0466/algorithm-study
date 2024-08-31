# https://leetcode.com/problems/unique-paths-ii/description/


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])

        dp = [[0] * N for _ in range(M)]

        for i in range(M):
            if obstacleGrid[i][0] == 1:
                break

            dp[i][0] = 1

        for i in range(N):
            if obstacleGrid[0][i] == 1:
                break

            dp[0][i] = 1

        for i in range(1, M):
            for j in range(1, N):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[M - 1][N - 1]
