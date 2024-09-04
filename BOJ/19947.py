# https://www.acmicpc.net/problem/19947

# 복리 투자
# 1년마다 5%이율을 얻는 투자 A
# 3년마다 20%의 이율을 얻는 투자 B
# 5년마다 35%의 이율을 얻는 투자 C

# 투자 방식은 매년 변경 가능
# 이율을 소수점 이하를 버림해서 받음

# DP로 풀이 가능할걸로 보임

H, Y = map(int, input().split())
dp = [0 for _ in range(Y + 1)]
dp[0] = H

for i in range(1, Y + 1):
    if i >= 5:
        dp[i] = max(dp[i - 1] * 1.05, dp[i - 3] * 1.2, dp[i - 5] * 1.35)
    elif i >= 3:
        dp[i] = max(dp[i - 1] * 1.05, dp[i - 3] * 1.2)
    else:
        dp[i] = dp[i - 1] * 1.05
    dp[i] = int(dp[i])

print(int(dp[Y]))
