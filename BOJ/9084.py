# https://www.acmicpc.net/problem/9084

# 동전의 화폐단위로 1원, 5원, 10원, 50원, 100원, 500원이 있다.
# N가지의 동전을 사용해 M원을 만들어야 한다.
# T만큼 테스트 케이스가 주어진다.

# 예시 케이스
# 2개
# 1원 2원
# 1000원 만들기
# 1원을 (2, 4, 6, ... 998) // 2 개까지 사용하고 나머지를 2원을 사용하면 된다.

import sys
T = int(sys.stdin.readline())

for _ in range(T):
	N = int(sys.stdin.readline())
	coins = list(map(int, sys.stdin.readline().split()))
	M = int(sys.stdin.readline())

	dp = [0] * (M+1)
	dp[0] = 1

	for coin in coins:
		for i in range(1, M+1):
			if (i >= coin):
				dp[i] += dp[i-coin]
	
	print(dp[M])