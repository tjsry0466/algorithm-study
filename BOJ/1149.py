# https://www.acmicpc.net/problem/1149

# 집이 N개 있음.
# 거리는 선분으로 나타낼 수 있고, 1번 집부터 집이 순서대로 있음.
# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 함
# 각각의 집을 발강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값 구하기

# 1번 집의 색은 2번집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 이상 N-1 이하)번 집의 색은 i-i, i+1번 집의 색과 같지 않아야 한다.

# 첫째 줄에 집의 수 N이 주어진다.
# 둘째 줄부터는 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한줄씩 주어진다.
# 집을 칠하는 비용은 1000보다 작거나 같은 자연수

# 접근 방법
# 앞뒤로 다른 값들이 들어가면 된다.
# 뭔가 백트래킹적인 요소가 들어가야될것 같기도 하다.
# 이전 값이 뭐였냐에 따라서 다음 값이 달라진다.

# 집의 수는 최대 1000.
# 제한 시간 0.5초. O(N^2)까지는 가능하다.
# DP + 백트래킹을 활용해서 최소비용을 DP 테이블에 저장해야겠다.

# 백트래킹을 활용한 풀이 (시간초과)

import sys

N = int(input())

arr = []
for i in range(N):
	arr.append(list(map(int, sys.stdin.readline().split())))

dp = [0] * (N + 1)

min_value = 999999999
def recr(x, exclude, v):
	global min_value
	if (x == N):
		min_value = min(min_value, v)
		return
	
	for i in range(3):
		if (i != exclude):
			recr(x+1, i, v + arr[x][i])

recr(0, -1, 0)

print(min_value)

# DP를 활용한 풀이

import sys

N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * 3 for _ in range(N)]

# 첫 번째 행 초기화
for i in range(3):
    dp[0][i] = arr[0][i]

# DP 테이블 채우기
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

# 최소값 출력
print(min(dp[N-1]))
