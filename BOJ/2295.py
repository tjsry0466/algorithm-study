# https://www.acmicpc.net/problem/2295

# 자연수로 이루어진 집합 U
# 세 수를 골랐을 때, 세 수의 합 D도 U안에 포함될 수 있다.
# 위 케이스에서 가장 큰 d를 찾는 문제

# 첫줄에 자연수 N
# 다음 N개의 줄게 U가 차례대로 주어짐
# U는 2억 이하의 자연수

# x, y, z 세 수를 놓고 찾으려고 하면 힘들고 O(N^3)으로 탐색해야 한다.
# x+y+z=r이 되어야 하므로 x+y=r-z로 바꾸어서 풀 수 있다.
# x+y로 만들 수 있는 값 r들을 미리 구한 후에 r에서 z를 뻈을때 sample에 포함되어 있으면 정답

import sys

input = sys.stdin.readline

N = int(input())
U = [int(input()) for _ in range(N)]
U.sort()
sample = set()

for i in U:
    for j in U:
        sample.add(i + j)

for i in range(N - 1, -1, -1):
    for j in range(i + 1):
        if U[i] - U[j] in sample:
            print(U[i])
            exit()
