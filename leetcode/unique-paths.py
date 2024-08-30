# https://leetcode.com/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * (n) for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                print(dp[i - 1][j] + dp[i][j - 1])
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


# 입력 데이터
m, n = 3, 7

# Solution 객체 생성 및 메서드 호출
solution = Solution()
result = solution.uniquePaths(m, n)

# 결과 출력
print(result)
