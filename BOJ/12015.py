# https://www.acmicpc.net/problem/12015

# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 문제
# 수열의 길이 N 최대 100만

from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))


dp = []

for i in A:
    k = bisect_left(dp, i)
    if len(dp) <= k:  # i가 자장 큰 숫자이면
        dp.append(i)
    else:
        dp[k] = i  # 자신보다 큰 수 중 최솟값과 대체
print(len(dp))
