# https://www.acmicpc.net/problem/2579

# 계단 오르는 문제
# 한칸 혹은 두칸만 이동할 수 있음

# 한칸은 한번만 이동 가능함.
# 최대 점수를 구하는 문제

# 2차원 배열 이용
# dp[층수][0] = 한칸으로 이동한 점수
# dp[층수][1] = 두칸으로 이동한 점수

N = int(input())

scores = [int(input()) for _ in range(N)]

if (N == 1):
	print(scores[0])
	exit()

dp = [[0,0] for _ in range(N)]
dp[0][0] = scores[0]
dp[0][1] = scores[0]
dp[1][0] = scores[1]
dp[1][1] = scores[0] +scores[1]
	
for i in range(2, N):
	score = scores[i]
	dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + score
	dp[i][1] = dp[i-1][0] + score

print(max(dp[N-1]))