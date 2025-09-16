n, m = map(int, input().split())

dp = [9999] * (m + 1)

arr = []

for i in range(n):
    x = int(input())
    if x <= m:
        arr.append(x)
        dp[x] = 1

for i in range(2, m + 1):
    for j in arr:
        if i - j > -1 and dp[i - j] != 9999:
            dp[i] = min(dp[i], dp[i - j] + 1)

print(dp[m] if dp[m] != 9999 else -1)
