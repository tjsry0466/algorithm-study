# https://www.acmicpc.net/problem/9461

# 삼각형이 나선 모양으로 놓여져 있음
# 첫 삼각형은 정삼각형 변의 길이는 1
# 가장 긴 변의 길이를 k라 했을 때, 그 변에 길이가 k인 정상감형 추가

# 파도반 수열 P(N)은 나선에 있는 정삼각형의 변의 길이이다.
# P(1)부터 P(10)까지 첫 10개 숫자는 1, 1, 1, 2, 2, 3, 4, 5, 7, 9이다. 

# N이 주어졌을 때, P(N)을 구하는 문제
# 따져보니까 dp[i] = dp[i-2] + dp[i-3] 이다.

N = int(input())
arr  = [int(input()) for _ in range(N)]

max_value = max(arr)

dp = [1] * (max_value + 1)

for i in range(3, max_value):
	dp[i] = dp[i-2] + dp[i-3]

for i in arr:
	print(dp[i-1])