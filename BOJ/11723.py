# https://www.acmicpc.net/problem/11723

# 비어있는 공집합 S가 주어질때, 아래 연상을 수행하는 프로그램 작성
# add x: S에 x를 추가한다. (단, S가 x에 이미 있는 경우 연산을 무시)
# remove x: S에서 x를 제거한다. (단, S에 x가 없는 경우 연산을 무시)
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다.
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다.
# all: S를 {1, 2, ..., 20}으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

import sys

input = sys.stdin.readline

N = int(input())
S = set()

for i in range(N):
    inputString = input().split()

    if len(inputString) == 1:
        if inputString[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    else:
        command, number = inputString
        x = int(number)
        if command == "add":
            S.add(x)
        elif command == "remove":
            S.discard(x)
        elif command == "check":
            print(1 if x in S else 0)
        elif command == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)
