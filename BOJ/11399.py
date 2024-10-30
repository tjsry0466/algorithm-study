# https://www.acmicpc.net/problem/11399

# ATM 앞에 N명의 사람들이 줄을 서있음.
# 사람은 1번부터 N번까지 번호가 매겨져 있음.
# i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분

N = int(input())
P = list(map(int, input().split()))

P.sort()

current = 0

for i in range(N):
    current += sum(P[: i + 1])

print(current)
