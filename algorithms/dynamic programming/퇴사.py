n = int(input())
arr = []

dp = [0] * (n + 1)

for i in range(n):
    t, p = map(int, input().split())
    arr.append((t, p))

for i in range(n):
    t, p = arr[i]

    # 상담을 선택하지 않는 경우: 다음 날의 최대값을 현재 날짜로 복사
    dp[i + 1] = max(dp[i + 1], dp[i])

    # 상담을 선택하는 경우
    nxt = i + t
    if nxt <= n:
        dp[nxt] = max(dp[nxt], dp[i] + p)


print(max(dp))
