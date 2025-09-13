# 첫째 줄에 수의 개수 N (2 ≤ N ≤ 11)
# 덧셈, 뺄셈, 곱셈, 나눗셈

from collections import deque

n = int(input())
seq = list(map(int, input().split()))
cal_input = list(map(int, input().split()))

min_value = 1e9
max_value = -1e9


def div_toward_zero(a, b):
    if a < 0:
        return -(abs(a) // b)
    return a // b


# BFS with queue over states: (index, current_value, add, sub, mul, div)
q = deque()
q.append((1, seq[0], cal_input[0], cal_input[1], cal_input[2], cal_input[3]))

while q:
    idx, cur, add, sub, mul, div = q.popleft()
    if idx == n:
        min_value = min(min_value, cur)
        max_value = max(max_value, cur)
        continue
    next_num = seq[idx]
    if add > 0:
        q.append((idx + 1, cur + next_num, add - 1, sub, mul, div))
    if sub > 0:
        q.append((idx + 1, cur - next_num, add, sub - 1, mul, div))
    if mul > 0:
        q.append((idx + 1, cur * next_num, add, sub, mul - 1, div))
    if div > 0:
        q.append((idx + 1, div_toward_zero(cur, next_num), add, sub, mul, div - 1))

print(max_value)
print(min_value)
