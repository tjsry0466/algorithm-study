# 바로 전칸에서 해당 칸에 오는 방법은 한가지
# 전전칸에서 해당 칸에 오는 방법은 2가지

n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 796796

print(dp[n])
