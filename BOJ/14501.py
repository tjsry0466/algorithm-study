# https://www.acmicpc.net/problem/14501

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

