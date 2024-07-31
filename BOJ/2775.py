# https://www.acmicpc.net/problem/2775

# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다.

# 주어지는 양의 정수 k와 n에 대해서 k층에 n호에는 몇명이 살고 있는지 출력
# 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

# TC 1
# 1층 3호, 2층 3호
# 6명, 10명

# 2층: (1호, 1명) (2호, 4명) (3호, 10명)
# 1층: (1호, 1명) (2호, 3명) (3호, 6명)
# 0층: (1호, 1명) (2호, 2명) (3호, 3명)

# bottom-up으로 공식을 구해보면 다음과 같다.
# dp[i] = sum(dp[i-1][0:i])

# 최대 층, 최대 호실을 구한 뒤 해당 층, 호실까지 dp 테이블을 구하고 정답을 출력하면 된다.

n = int(input())

arr = []

max_floor = 0
max_ho = 0

for i in range(n):
	floor = int(input())
	ho = int(input())

	max_floor = max(max_floor, floor)
	max_ho = max(max_ho, ho)

	arr.append([floor, ho])

if max_floor == 0:
	print(max_ho)
	exit()

dp = [[0 for _ in range(max_ho)] for _ in range(max_floor + 1)]
dp[0] = [i + 1 for i in range(max_ho)]

for i in range(1, max_floor + 1):
	for j in range(max_ho):
		dp[i][j] = sum(dp[i - 1][:j + 1])

for floor, ho in arr:
	print(dp[floor][ho - 1])


