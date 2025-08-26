# 정렬 후 앞에부터 순회하면서 특정 수 만큼 쌓이면 그룹으로 묶기

n = int(input())
data = list(map(int, input().split()))

data.sort()
groups = 0
count = 0
for f in data:
    count += 1
    if count >= f:
        groups += 1
        count = 0

print(groups)
