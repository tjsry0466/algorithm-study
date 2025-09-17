count = int(input())

for i in range(count):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    board = []

    for i in range(0, (n * m) + 1, m):
        board.append(arr[i : i + m])

    dp = [[0] * m for i in range(n)]
    dp[0][0] = board[0][0]
    dp[1][0] = board[1][0]
    dp[2][0] = board[2][0]

    for i in range(1, m):  # 열
        for j in range(n):  # 행
            dp[j][i] = max(dp[j][i], dp[j][i - 1] + board[j][i])
            if 0 <= j - 1 < n:
                dp[j][i] = max(dp[j][i], dp[j - 1][i - 1] + board[j][i])
            if 0 <= j + 1 < n:
                dp[j][i] = max(dp[j][i], dp[j + 1][i - 1] + board[j][i])

    print(max(row[-1] for row in dp))
