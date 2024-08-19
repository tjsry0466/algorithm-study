# https://www.acmicpc.net/problem/2240

# 매 초마다 두개의 나무 중 하나의 나무에서 열매가 떨어지게 된다.
# 자두는 T초 동안 떨어진다. 최대 W번만 움직이고 싶다.
# 매 초마다 어느 나무에서 자두가 떨어질지에 대한 정보가 주어졌을 때, 자두가 받을 수 있는 자두의 개수를 구해내는 프로그램을 작성하는 문제
# 첫 위치는 1번에서 시작한다.

# 접근 방법
# 이동 하고 얻는다.
# 이동 안하고 [얻거나 못얻는다]

# 1. 현재 위치를 유지하는 경우
# 1번 위치에 있다면 1번 나무에서 떨어질 때에만 + 1
# dp[t][w] = dp[t-1][w] + 1
# 2번 위치에 있다면 2번 나무에서 떨어질 때에만 + 1
# dp[t][w] = dp[t-1][w] + 1

# 2. 위치를 바꾸는 경우
# 1번 나무에서 2번 나무로 이동하는 경우, 자두가 2번 나무에서 떨어질 때에만 + 1
# dp[t][w] = dp[t-1][w-1] + 1
# 2번 나무에서 1번 나무로 이동하는 경우, 자두가 1번 나무에서 떨어질 때에만 + 1
# dp[t][w] = dp[t-1][w-1] + 1

# 왜 이렇게 접근했는가?
# 최적 부분 구조: 자두가 떨어지는 매 순간, 최적의 선택을 한다는 점에서 이 문제는 동적 계획법(DP)을 적용할 수 있습니다. 각 단계에서의 최적해가 전체 문제의 최적해를 구성합니다.
# 중복 계산 제거: DP를 통해 각 순간마다 이전 결과를 기반으로 최적의 값을 계산함으로써, 중복된 계산을 피할 수 있습니다.
# 상태 전이: 자두의 위치와 이동 횟수에 따른 상태를 고려하여, 이전 상태에서 다음 상태로의 최적해를 도출합니다.
# 단순 반복문: 이중 반복문을 사용하여 모든 경우의 수를 체크하면서, 현재 시점에서 최적의 선택을 할 수 있도록 dp[t][w]를 갱신합니다.

import sys

input = sys.stdin.readline

T, W = map(int, input().split())
drops = [0] + [int(input()) for _ in range(T)]
dp = [[0] * (W + 1) for _ in range(T + 1)]

# bottom_up dp
dp[1][0], dp[1][1] = drops[1] % 2, drops[1] // 2
for t in range(2, T + 1):
		for w in range(W + 1):
				j = drops[t] % 2 if w % 2 == 0 else drops[t] // 2
				dp[t][w] = max(dp[t - 1][0:w + 1]) + j
print(max(dp[-1]))

# ---

import sys
input = sys.stdin.readline

T, W = map(int, input().split())
drops = [0] + [int(input()) for _ in range(T)]
dp = [[0] * (W + 1) for _ in range(T + 1)]

# 초기 상태
for w in range(W + 1):
    if drops[1] == 1:
        dp[1][w] = 1 if w % 2 == 0 else 0
    else:
        dp[1][w] = 1 if w % 2 == 1 else 0

# DP 갱신
for t in range(2, T + 1):
    for w in range(W + 1):
        if drops[t] == 1:
            dp[t][w] = max(dp[t-1][w], dp[t-1][w-1] if w > 0 else 0) + (1 if w % 2 == 0 else 0)
        else:
            dp[t][w] = max(dp[t-1][w], dp[t-1][w-1] if w > 0 else 0) + (1 if w % 2 == 1 else 0)

print(max(dp[T]))

# ---

import sys
input = sys.stdin.readline

T, W = map(int, input().split())
drops = [0] + [int(input()) for _ in range(T)]
dp = [[0] * (W + 1) for _ in range(T + 1)]

for t in range(1, T + 1):
    for w in range(W + 1):
        if drops[t] == 1:
            dp[t][w] = max(dp[t-1][w], dp[t-1][w-1] if w > 0 else 0) + (1 if w % 2 == 0 else 0)
        else:
            dp[t][w] = max(dp[t-1][w], dp[t-1][w-1] if w > 0 else 0) + (1 if w % 2 == 1 else 0)

print(max(dp[T]))

