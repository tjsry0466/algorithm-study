n = int(input())

ugly = [0] * n
ugly[0] = 1

i2 = i3 = i5 = 0

for i in range(1, n):
    # 다음 후보 계산
    next2 = ugly[i2] * 2
    next3 = ugly[i3] * 3
    next5 = ugly[i5] * 5

    # 가장 작은 값을 선택
    ugly[i] = min(next2, next3, next5)

    # 선택한 값과 같은 포인터들을 증가
    if ugly[i] == next2:
        i2 += 1
    if ugly[i] == next3:
        i3 += 1
    if ugly[i] == next5:
        i5 += 1

print(ugly[n - 1])
