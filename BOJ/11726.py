# https://www.acmicpc.net/problem/11726

# 2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
# n은 1부터 1000

# 작은 부분 문제로 어떻게 나뉘어지는지 고려해야한다.

# n까지 채웠을 때 가능한 경우의 수를 누적해가고, 누적한 DP 테이블을 이용해 값을 구한다.
# 중요한건 모든 경우의 수에 대해서 값을 구해야 한다.

N = int(input())
if N == 0:
    print(0)
    exit()
elif N == 1:
    print(1)
    exit()

dp = [0 for _ in range(N)]
dp[0] = 1
dp[1] = 2

for i in range(2, N):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N-1] % 10007)

