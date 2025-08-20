# 단순하게 푸는 예시

n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    if m == 0:
        break

    for i in range(k):
        result += first
        m -= 1
    if m == 0:
        break

    result += second
    m -= 1

print(result)
