n = int(input())

arr = []

for i in range(n):
    nums = list(map(int, input().split()))
    arr.append(nums)

if n == 1:
    print(arr[0][0])
    exit()

dp = [[0] * n for i in range(n)]
dp[0][0] = arr[0][0]
dp[1][0] = arr[0][0] + arr[1][0]
dp[1][1] = arr[0][0] + arr[1][1]


for i in range(2, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + arr[i][j])
        elif j == i:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + arr[i][j])
        else:
            leftSum = dp[i - 1][j - 1] + arr[i][j]
            rightSum = dp[i - 1][j] + arr[i][j]

            dp[i][j] = max(dp[i][j], leftSum, rightSum)

print(max(dp[-1][:]))
