# https://www.acmicpc.net/problem/2302

# 어떤 극장의 좌석이 한 줄로 되어 있음.
# 1번부터 N번까지 존재
# 입장권에 쓰여 있는 곳에 앉아야 하는데 왼쪽 또는 오른쪽으로 좌석을 옮길 수 있음

# VIP회원들은 반드시 자기 좌석에만 앉아야 한다.
# 모든 좌석이 다 팔리고 VIP 회원들의 좌석 번호들이 주어졌을 때, 서로 다른 좌석에 앉는 경우의 수를 구하는 문제

# 좌석의 개수 N (1부터 40이하)
# 고정석의 수 M (0이상 N이하)
# 방법의 가지수는 20억을 넘지 않음

# 접근 방법
# 고정석을 기준으로 각각을 DP로 구하면 됨.
# 전체 값 대상으로 DP를 구하고 VIP석을 기준으로 나눠서 DP테이블의 값을 참조하면 됨.

import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
vips = [int(input()) for _ in range(M)]

dp = [1] * (N+1)
# 기저상태 정의
dp[1] = 1
if N > 1:
  dp[2] = 2
  
# 점화식: dp[n] = dp[n-1] + dp[n-2]
for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

answer = 1
pre = 0
for vip in vips:
    # dp[vips - 1 - pre]는
		# 4 - 1 - 0 = 3 (첫번쨰 구간은 3개)
    # 7 - 1 - 4 = 2 (두번째 구간은 2개)
    answer *= dp[vips - 1 - pre] 
    pre = vips
    
# dp[N-pre]는 9 - 7 = 2 (세번째 구간은 3개)
answer *= dp[N-pre]

print(answer)