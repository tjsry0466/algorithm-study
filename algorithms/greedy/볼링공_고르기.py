# 순서 상관없이 조합을 구하고 수가 같지 않은 경우 카운트

from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))

result = 0

for i in combinations(data, 2):
    if i[0] != i[1]:
        result += 1

print(result)
