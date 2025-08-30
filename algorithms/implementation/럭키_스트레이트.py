# 수를 반절로 나누어 각각의 숫자의 합이 동일하다면 LUCKY 아니면 READY

n = input()

left = n[: len(n) // 2]
right = n[len(n) // 2 :]

left_sum = sum(map(int, left))
right_sum = sum(map(int, right))

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
