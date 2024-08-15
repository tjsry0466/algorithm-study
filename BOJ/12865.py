# https://www.acmicpc.net/problem/12865

# 배낭 문제

# 점화식
# dp[인덱스][무게] = 가치
# dp[i-1][j]에 데이터가 있고 현재 무게를 더했을때 K를 초과하지 않으면
# 넣는 경우 dp[i][j+items[i][0]] = max(dp[i-1][j]+items[i][1], dp[i][j])
# 안넣는 경우 dp[i][j] = dp[i-1][j]

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N+1):
		weight, value = items[i-1]
		for j in range(K + 1):
			if j >= weight:
				dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
			else:
				dp[i][j] = dp[i-1][j]

print(dp[N][K])
