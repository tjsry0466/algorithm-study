# https://www.acmicpc.net/problem/11052

# 8종류의 등급의 색이 칠해져 있는 카드가 있다.
# 카드는 카드팩의 형태로만 구매가 가능하고 1개부터 N개가 포함된 카드팩 N가지가 존재한다.
# 카드의 개수가 적더라도 가격이 비싸면 높은 등급이 많이 들어 있을거라 생각한다.
# 최대한 많은 돈을 지불해서 카드 N개를 구매. 카드가 i개 포함된 카드팩의 가격은 P(i)원이다.

# 점화식은 dp[i] = max(dp[i], dp[i-j] + p[j])

N = int(input())
p = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)

for i in range(1, N+1):
	for j in range(1, i+1):
		dp[i] = max(dp[i], dp[i-j] + p[j])

print(dp[N])