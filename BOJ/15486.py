# https://www.acmicpc.net/problem/15486

# 퇴사하기 전에 남은 N일 동안 최대한 많은 상담을 하려고 한다.
# 각각의 상담은 상담을 완료하는데 걸리는 기간T(i)와 상담을 했을 때 받을 수 있는 금액 P(i)로 이루어져 있다.

import sys
sys.setrecursionlimit(99999999)

input = sys.stdin.readline

def recur(idx):
	global answer

	if idx == N+1:
		return 0
	if idx > N+1:
		return -999999999
	if dp[idx] != -1:
		return dp[idx]
	
	dp[idx] = max(recur(idx + table[idx][0]) + table[idx][1], recur(idx+1))

	return dp[idx]


N = int(input())

table = [[] for _ in range(N+1)]
for i in range(1, N+1):
	a, b = map(int, input().split())
	table[i] = [a, b]

dp = [-1 for _ in range(N+1)]

ans = recur(1)
print(ans)