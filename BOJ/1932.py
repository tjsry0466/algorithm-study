# https://www.acmicpc.net/problem/1932

#         7
#       3   8
#     8   1   0
#   2   7   4   4
# 4   5   2   6   5

# 위 그림은 크기가 5인 정수 삼각형의 모습
# 맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때
# 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램 작성
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것만 선택할 수 있음.
# 삼각형의 크기는 1 이상 500 이하. 수의 범위는 0 이상 9999 이하

N = int(input())

arr = []
for i in range(N):
	arr.append(list(map(int, input().split())))

dp = []
for i in range(1, N+1):
	dp.append([0 for _ in range(i)])

dp[0][0] = arr[0][0]

# print(arr)
# print(dp)

for i in range(1, N):
	for j in range(i + 1):
		if (j == 0): # 첫번째
			dp[i][j] = arr[i][j] + dp[i-1][j]
		elif (i == j): # 마지막
			dp[i][j] = arr[i][j] + dp[i-1][j-1] 
		else:
			dp[i][j] = arr[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[N-1]))