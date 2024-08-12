# https://www.acmicpc.net/problem/2302

# 어떤 극장의 좌석이 한 줄로 되어 있음.
# 1번부터 N번까지 존재
# 입장권에 쓰여 있는 곳에 앉아야 하는데 왼쪽 또는 오른쪽으로 좌석을 옮길 수 있음

# VIP회원들은 반드시 자기 좌석에만 앉아야 한다.
# 모든 좌석이 다 팔리고 VIP 회원들의 좌석 번호들이 주어졌을 때, 서로 다른 좌석에 앉는 경우의 수를 구하는 문제

# 좌석의 개수 N (1부터 40이하)
# 고정석의 수 M (0이상 N이하)
# 방법의 가지수는 20억을 넘지 않음

# 접근 방법
# 고정석을 기준으로 양옆으로 새롭게 구해야함. 칸막이 같은 느낌
# 특정 값을 사용했는지 판단하는 배열을 하나 두고 관리하면 좋을 것 같음.
# 고정석은 미리 사용해두고 시작해도 괜찮을 듯.
# 일단 다 해보고 안되면 갈아끼우는 식으로 해야할지? -> 백트래킹 적용

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
vip = [int(sys.stdin.readline()) for _ in range(m)]

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
if n >= 2:
    dp[2] = 2

# 점화식: dp[n] = dp[n - 1] + dp[n - 2]
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

answer = 1  # 경우의 수
if m > 0:
    pre = 0
    for j in range(m):
        # vip[j] - 1 - pre가 음수가 되지 않도록 체크
        if vip[j] - 1 - pre >= 0:
            answer *= dp[vip[j] - 1 - pre]
        pre = vip[j]
    
    # 마지막 구간 처리
    if n - pre >= 0:
        answer *= dp[n - pre]
else:
    answer = dp[n]

print(answer)
