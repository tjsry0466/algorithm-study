# https://www.acmicpc.net/problem/2565

# 두 전봇대 A와 B사이에 전깃줄이 교차하는 경우가 발생
# 몇 개의 전깃줄을 없애 전깃줄이 교차하지 않도록 만드는 문제
# 전깃줄의 개수와 전깃줄들이 두 전봇대에 연결되어 있는 위치의 번호가 주어질 때, 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전길줄의 최소 개수를 구해야 한다.
# 전깃줄의 개수는 100 이하의 자연수
# 위치의 번호는 500 이하의 자연수


N = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(N)])
dp = [1 for _ in range(N)]

for i in range(N):
	for j in range(i):
		if (arr[i][1] > arr[j][1]):
			dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))