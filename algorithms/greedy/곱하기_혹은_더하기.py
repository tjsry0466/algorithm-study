# 접근 방법
# S의 길이가 최대 20
# 모든 경우의 수를 구해서 계산해봐도 괜찮을 것 같다.

from itertools import product

input_str = input()

permutations_list = product("x+", repeat=len(input_str) - 1)

answer = 0

for permutation in permutations_list:
    result = int(input_str[0])
    for idx, i in enumerate(permutation):
        if i == "x":
            result *= int(input_str[idx + 1])
        else:
            result += int(input_str[idx + 1])
    answer = max(answer, result)

print(answer)
