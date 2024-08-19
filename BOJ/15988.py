# https://www.acmicpc.net/problem/15988
# 정수 N을 1, 2, 3의 합으로 만드는 경우의 수를 구하는 문제
# 정답을 1000000009로 나눈 나머지를 출력

# DP의 크기는 MAX(arr)+1
# DP[0] = 1
# DP[1] = 1
# DP[2] = 2

# 점화식
# DP[i] = DP[i-3] + DP[i-2] + DP[i-1]

N = int(input())

arr = [int(input()) for _ in range(N)]
max_arr = max(arr)
DP = [0] * (max_arr+1)
DP[0] = 1
DP[1] = 1
DP[2] = 2

for i in range(3, max_arr+1):
	DP[i] = (DP[i-3] + DP[i-2] + DP[i-1]) % 1000000009

for i in arr:
	print(DP[i])